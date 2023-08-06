from .host import Vote, VotifierServer


with VotifierServer(port=8192) as server:
    while True:
        vote = server.wait_for_vote()
        print(f'New vote: {vote.json(indent=2)}')
