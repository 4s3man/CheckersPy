from enum import Enum
class Color(Enum):
    WHITE = 'white'
    BLACK = 'black'

    def opposite(self):
        return Color('black') if self.name == 'WHITE' else Color('white')
