from bundles.Connection import Connection

class Ranking():
    connection = None
    gameTypes = 'HOT_SEATS', 'VS_COMPUTER', 'THROUGH_NET'
    results = 'WIN', 'LOST', 'DRAW'

    WIN = 'WIN'
    LOST ='LOST'
    DRAW = 'DRAW'

    HOT_SEATS = 'HOT_SEATS'
    VS_COMPUTER = 'VS_COMPUTER'
    THROUGH_NET = 'THROUGH_NET'

    def __init__(self):
        self.connection = Connection()

    def increment(self, gameType, result, userId):
        self.checkGameType(gameType)
        self.checkResult(result)

        currentResult = self.getEndResultCount(result, userId, gameType)
        if currentResult == None:
            query = 'INSERT INTO RANKING (USERID, GAME_TYPE, {result}) VALUES (?, ?, ?)'.format(result=result)
            self.connection.execute(query, (userId, gameType, 1))
        else:
            currentResult += 1
            query = 'UPDATE RANKING SET {result} = ? WHERE USERID = ? AND GAME_TYPE = ?'.format(result=result)
            self.connection.execute(query, (currentResult, userId, gameType))

    def find_all(self):
        return self.connection.query_db('SELECT * FROM RANKING', '')

    def getEndResultCount(self, result, userId, gameType):
        query = 'SELECT {result} FROM RANKING WHERE USERID = ? and GAME_TYPE = ?'.format(result=result)
        return self.connection.get_scalar_result(query, (userId, gameType))

    def checkResult(self, result):
        if result not in Ranking.results:
            raise Exception('Invalid argument: result')

    def checkGameType(self, result):
        if result not in Ranking.gameTypes:
            raise Exception('Invalid argument: gameType')
