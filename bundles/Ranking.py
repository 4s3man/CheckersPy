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

        # if not self.last_result_older_than_40s(gameType, userId):
        #     return

        currentResult = self.getEndResultCount(result, userId, gameType)
        if currentResult == None:
            query = 'INSERT INTO RANKING (USERID, GAME_TYPE, {result}) VALUES (?, ?, ?)'.format(result=result)
            self.connection.execute(query, (userId, gameType, 1))
        else:
            currentResult += 1
            query = 'UPDATE RANKING SET {result} = ?, LAST_UPDATE = julianday(\'now\') WHERE USERID = ? AND GAME_TYPE = ?'.format(result=result)
            self.connection.execute(query, (currentResult, userId, gameType))

    def find_top_20_for_game(self, game_type):
        self.checkGameType(game_type)
        return self.connection.query_db('''SELECT USER.LOGIN, RANKING.GAME_TYPE, RANKING.WIN, RANKING.LOST, RANKING.DRAW
        FROM RANKING INNER JOIN USER ON RANKING.USERID = USER.ID
        WHERE RANKING.GAME_TYPE = ?
        ORDER BY (WIN - LOST) DESC LIMIT 20''', [game_type])

    def find_for_user(self, user_id):
        if user_id == None:
            return None

        return self.connection.query_db('SELECT * FROM RANKING WHERE USERID = ?', [user_id])

    def getEndResultCount(self, result, userId, gameType):
        query = 'SELECT {result} FROM RANKING WHERE USERID = ? and GAME_TYPE = ?'.format(result=result)
        return self.connection.get_scalar_result(query, (userId, gameType))

    # def last_result_older_than_40s(self, game_type, user_id):
    #     self.checkGameType(game_type)
    #     result = self.connection.query_db('''SELECT 40 < (julianday('now') - LAST_UPDATE) FROM RANKING WHERE USERID = ? AND GAME_TYPE = ?''', [user_id, game_type])
    #     print(result)
        # return bool(result[0]) if result else False

    def checkResult(self, result):
        if result not in Ranking.results:
            raise Exception('Invalid argument: result')

    def checkGameType(self, result):
        if result not in Ranking.gameTypes:
            raise Exception('Invalid argument: gameType')
