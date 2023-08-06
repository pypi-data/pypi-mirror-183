import asyncio

import pytest
from aiovotifier import VotifierClient

from votifier_py import Vote, VotifierServer


@pytest.mark.asyncio
async def test_server() -> None:
    server: VotifierServer = None  # type: ignore
    try:
        port = 9998
        server = VotifierServer(port=port).start()

        with open('nuvotifier.secret', 'r') as f:
            token = f.read()

        client = VotifierClient('127.0.0.1', port=port, service_name='TestService', secret=token)

        promise = await client.nu_vote('user', '10.0.0.1')

        vote: Vote = server.wait_for_vote()
        assert vote.username == 'user'
        assert promise.get('status', '') == 'ok'
    finally:
        server.stop()
