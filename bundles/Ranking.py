from bundles.Connection import Connection;

class Ranking():
    GAMETYPE = 'VS_COMPUTER', 'THROUGH_NET'
    connection = None

    def __init__(self):
        self.connection = Connection()

    def increment(self, gameType, result):
        self.connection.execute()