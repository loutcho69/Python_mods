from abc import ABC, abstractmethod
from .class_name import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self):
        pass
    @abstractmethod
    def create_evolved(self):
        pass

class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()
    def create_evolved(self)-> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()
    def create_evolved(self) ->Creature:
        return Torragon()
