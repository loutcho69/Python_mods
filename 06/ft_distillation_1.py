import alchemy


def main() -> None:
    print("=== Distillation 0 ===\n")
    print("Using: 'import alchemy' structure to access potions\n")
    print(f"Testing strength_potion: {alchemy.potions.strenght_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")


main()
