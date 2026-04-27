from ex0 import factory

Flame = factory.FlameFactory()
Aqua = factory.AquaFactory()


def creation(facto: factory.CreatureFactory) -> None:
    mob = facto.create_base()
    print(mob.describe())
    print(mob.attack())
    mob = facto.create_evolved()
    print(mob.describe())
    print(mob.attack())


def fight(facto1: factory.FlameFactory, facto2: factory.AquaFactory) -> None:
    mob1 = facto1.create_base()
    mob2 = facto2.create_base()
    print(mob1.describe())
    print("vs.")
    print(mob2.describe())
    print("fight!")
    print(mob1.attack())
    print(mob2.attack())


def main() -> None:
    print("Testing factory")
    creation(Flame)
    print("\nTesting factory")
    creation(Aqua)
    print("\nTesting battle")
    fight(Flame, Aqua)


main()
