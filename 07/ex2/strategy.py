from abc import ABC, abstractmethod
from ex1 import capability, creature

class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self,creature)-> bool:
        pass
    @abstractmethod
    def act(self, creature)-> None:
        pass

class NormalStrategy(BattleStrategy):
    def is_valid(self,creature)->bool:
        return True
    def act(self, creature)-> None:
        if self.is_valid(creature):
            print(creature.attack())

class AgressiveStrategy(BattleStrategy):
    def is_valid(self, creature)->bool:
        return hasattr(creature,'transform')
    def act(self, creature)-> None:
        if self.is_valid(creature):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise ValueError ("Invalid parameters")

class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature)->bool:
        return hasattr(creature,'heal')
    def act(self, creature)-> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            raise ValueError ("Invalid parameters")