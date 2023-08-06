from __future__ import annotations

import hashlib
import hmac
import json
import secrets
import socketserver
import struct
import threading
from base64 import b64encode
from pathlib import Path
from queue import Queue
from socket import socket as Socket

from pydantic.main import BaseModel


class Vote(BaseModel):
    username: str
    serviceName: str
    timestamp: int
    address: str
    challenge: str
    uuid: str | None = None


class VoteRequest(BaseModel):
    signature: str
    payload: str

    def get_payload(self):
        return Vote(**json.loads(self.payload))


class NuvotifierHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.nuvote()

    def get_private_key(self) -> bytes:
        with open('nuvotifier.secret', 'rb') as f:
            return f.read().strip(b'\n ')

    def make_signature(self, payload: bytes):
        private_key = self.get_private_key()
        return b64encode(hmac.digest(private_key, payload, hashlib.sha256)).decode()

    def read_vote_request(self, length: int) -> VoteRequest:
        payload_bytes = self.request.recv(length)
        payload_str = payload_bytes.decode()
        data = json.loads(payload_str)
        return VoteRequest(**data)

    def nuvote(self) -> None:
        self.request: Socket
        self.server: VotifierServer  # type: ignore
        self.request.settimeout(3)

        # Handshake reply
        challenge = secrets.token_hex(16)
        self.request.sendall(b'VOTIFIER 2 ' + challenge.encode())

        # Read preamble
        header = self.request.recv(4)
        start, length = struct.unpack(">HH", header)
        assert start == 0x733A, f'Expected 0x733A preamble, got: {start}'

        # Read payload
        vote_request: VoteRequest = self.read_vote_request(length)
        payload: Vote = vote_request.get_payload()

        # Validate challenge-response
        assert (
            payload.challenge == challenge
        ), f'Challenge mismatch. Expected: "{challenge}". Received: "{payload.challenge}"'
        expected_signature = self.make_signature(vote_request.payload.encode())
        assert expected_signature == vote_request.signature, f'Token mismatch. Got signature "{vote_request.signature}"'

        # process vote and send response
        self.server._vote_queue.put(payload)
        self.request.sendall(b'{"status": "ok"}')
        print('Vote cast.')


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class VotifierServer:
    def __init__(self, ip: str = 'localhost', port: int = 8192, token_file: str | Path = 'nuvotifier.secret') -> None:
        self.port: int = port
        self.ip: str = ip
        self.token_file: Path = Path(token_file)
        self._vote_queue: Queue[Vote] = Queue()
        if not self.token_file.exists():
            VotifierServer.generate_token(self.token_file)

        self._server = ThreadedTCPServer((self.ip, self.port), NuvotifierHandler)
        self._server._vote_queue = self._vote_queue  # type: ignore

    def wait_for_vote(self, timeout: float | None = None) -> Vote:
        return self._vote_queue.get(block=True, timeout=timeout)

    @classmethod
    def generate_token(cls, file: str | Path):
        with open(file, 'w') as f:
            f.write(secrets.token_urlsafe(260))

    def _start(self) -> None:
        with self._server:
            self._server.serve_forever()

    def start(self) -> VotifierServer:
        thread = threading.Thread(target=self._start)
        thread.daemon = True
        thread.start()
        print('Server started')
        return self

    def stop(self) -> None:
        print('Stopping server')
        self._server.shutdown()
        print('Server stopped')

    def __enter__(self) -> VotifierServer:
        self.start()
        return self

    def __exit__(self, *_):
        self.stop()
