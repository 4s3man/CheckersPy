from abc import ABC

class Game_Obj(ABC):
    def __eq__(self, compare)->bool:
        if not isinstance(compare, type(self)): return False
        for key in self.__dict__.keys():
            if getattr(self, key, None) != getattr(compare, key, None): return False
        return True

    def __neq__(self, compare)->bool:
        return not self.__eq__(compare)
