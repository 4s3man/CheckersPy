from bundles.Connection import Connection
from re import compile, match
class User:
    connection = None
    validationRegex = '^[a-zA-Z0-9_%!@#$^&*<>]+$'

    def __init__(self):
        self.connection = Connection()

    def create(self, login, password):
        self.connection.execute("INSERT INTO USER (LOGIN, PASSWORD) VALUES ( ?, ? )", (login, password))

    def login_already_exists(self, login):
        return bool(
            self.connection.query_db('SELECT ID FROM USER WHERE LOGIN = ?', (login,))
        )

    def get_user_dict(self, login, password):
        user_data = self.connection.query_db('SELECT ID, LOGIN FROM USER WHERE LOGIN = ? AND PASSWORD = ?', (login, password), True)
        return {'id':user_data[0], 'login':user_data[1]} if user_data is not None else None

    def validate(self, input):
        pattern = compile(User.validationRegex)
        return match(pattern, input)

    def getAllowedChars(self):
        return User.validationRegex.strip('^[]$+')
