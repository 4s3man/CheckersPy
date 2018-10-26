class Coin:
    id = 0
    color = ''
    foreward = 0
    type = ''
    moves = {}
    y = 0
    x = 0
    def __init__(self, color, id, type='coin'):
        self.color = color
        self.id = id
        self.type = type

    def set_foreward_vector(self, vector):
        self.foreward = vector

    def html(self):
        return '<span id="%s" class="%s coin--%s"></span>' % (
            self.color + str(self.id), self.type, self.color)
