from __future__ import annotations
from abc import abstractmethod

import hashlib
import hmac
import json
import secrets
import struct
from base64 import b64encode
from pathlib import Path
from queue import Queue
from socket import socket as Socket
from socketserver import TCPServer, BaseRequestHandler, ThreadingMixIn
from threading import Event, Thread
import logging

from pydantic.main import BaseModel


logger = logging.getLogger("votifier_py")


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


class NuvotifierHandler(BaseRequestHandler):
    def handle(self):
        self.nuvote()

    def make_signature(self, payload: bytes):
        private_key: bytes = self.server._token  # type: ignore
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
        if start != 0x733A:
            raise Exception(f'Expected 0x733A preamble, got: {start}')

        # Read payload
        vote_request: VoteRequest = self.read_vote_request(length)
        payload: Vote = vote_request.get_payload()

        # Validate challenge-response
        if payload.challenge != challenge:
            raise Exception(f'Challenge mismatch. Expected: "{challenge}". Received: "{payload.challenge}"')
        expected_signature = self.make_signature(vote_request.payload.encode())

        if expected_signature != vote_request.signature:
            raise Exception(f'Token mismatch. Got signature "{vote_request.signature}"')

        # process vote and send response
        self.server._vote_queue.put(payload)
        self.request.sendall(b'{"status": "ok"}')
        logger.info(f'Vote cast by "{payload.username}"')


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    def __init__(self, ip: str, port: int, token: bytes) -> None:
        self.shutdown_event = Event()
        self._main_thread: Thread | None = None
        self._vote_queue: Queue[Vote] = Queue()
        self._token: bytes = token
        TCPServer.__init__(self, (ip, port), NuvotifierHandler)

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, *_):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def server_bind(self) -> None:
        self.allow_reuse_address = True
        super().server_bind()
        logger.debug(f'Votifier server listening on {self.server_address[0]}:{self.server_address[1]}')

    def shutdown(self) -> None:
        self.shutdown_event.set()
        TCPServer.shutdown(self)
        ThreadingMixIn.server_close(self)
        if self._main_thread is not None:
            del self._main_thread
            self._main_thread = None

    def start_serving(self, poll_interval: float = 0.2) -> None:
        '''Non-blocking start.'''
        if self._main_thread is not None:
            raise Exception('Attempting to start already running server. Aborting.')
        # Set flag
        self._poll_interval = poll_interval
        self._main_thread = Thread(target=self.serve_forever)
        self._main_thread.start()


class VotifierServer(ThreadedTCPServer):
    def __init__(self, ip: str = 'localhost', port: int = 8192, token_file: str | Path = 'nuvotifier.secret') -> None:
        self.port: int = port
        self.ip: str = ip
        self.token_file: Path = Path(token_file)
        if not self.token_file.exists():
            VotifierServer.generate_token(self.token_file)

        token = self.get_private_key(Path(token_file))
        ThreadedTCPServer.__init__(self, ip=ip, port=port, token=token)

    def get_private_key(self, path: Path) -> bytes:
        with open(path, 'rb') as f:
            return f.read().strip(b'\n ')

    def wait_for_vote(self, timeout: float | None = None) -> Vote:
        return self._vote_queue.get(block=True, timeout=timeout)

    @classmethod
    def generate_token(cls, file: str | Path):
        with open(file, 'w') as f:
            f.write(secrets.token_urlsafe(130))

    def _start(self) -> None:
        with self:
            self.serve_forever()

    def start(self) -> VotifierServer:
        self.start_serving()
        logger.info('Server started')
        return self

    def stop(self) -> None:
        '''Stop votifier server'''
        logger.info('Stopping server')
        self.shutdown()
        logger.info('Server stopped')

    def __enter__(self) -> VotifierServer:
        self.start()
        return self

    def __exit__(self, *_):
        self.stop()
