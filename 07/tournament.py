from ex0.factory import FlameFactory, AquaFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import NormalStrategy,AgressiveStrategy,DefensiveStrategy


def battle(opponents: list) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
 
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]
 
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()
 
            print("\n* Battle *")
            print(f"{creature_a.describe()} vs. {creature_b.describe()}")
            print("now fight!")
 
            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
 
if __name__ == "__main__":

    print("Tournament 0 (basic)")
    battle([
        (FlameFactory(),           NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print()
    print("Tournament 1 (error)")
    battle([
        (FlameFactory(),           AgressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print()
    print("Tournament 2 (multiple)")
    battle([
        (AquaFactory(),              NormalStrategy()),
        (HealingCreatureFactory(),   DefensiveStrategy()),
        (TransformCreatureFactory(), AgressiveStrategy()),
    ])
