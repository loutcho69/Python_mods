from ex0 import factory
from ex1 import creature 
from ex0.class_name import Creature


class HealingCreatureFactory(factory.CreatureFactory):
    def create_base(self) -> Creature:
        return creature.Sproutling()
    def create_evolved(self) ->Creature:
        return creature.Bloomelle()

class TransformCreatureFactory(factory.CreatureFactory):
    def create_base(self) -> Creature:
        return creature.Shiftling()
    def create_evolved(self) ->Creature:
        return creature.Morphagon()
