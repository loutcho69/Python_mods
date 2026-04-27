from ex1 import factory


def main():
    heal = factory.HealingCreatureFactory()

    mob1 = heal.create_base()
    mob2 = heal.create_evolved()
    print("Testing creature with healing capability")
    print("base:")
    print(mob1.describe())
    print(mob1.attack())
    print(mob1.heal())
    print("evolved:")
    print(mob2.describe())
    print(mob2.attack())
    print(mob2.heal())
    print("\nTesting creature with transform capability")
    print("base:")

    trans = factory.TransformCreatureFactory()
    mob3 = trans.create_base()
    mob4 = trans.create_evolved()
    print(mob3.describe())
    print(mob3.attack())
    print(mob3.transform())
    print(mob3.attack())
    print(mob3.revert())
    print("evolved:")
    print(mob4.describe())
    print(mob4.attack())
    print(mob4.transform())
    print(mob4.attack())
    print(mob4.revert())


main()
