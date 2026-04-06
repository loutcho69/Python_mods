from alchemy import potions


def main() -> None:
    print("=== Distillation 0 ===\n")
    print("Direct access to alchemy/potions.py\n")
    print(f"Testing strength_potion: {potions.strenght_potion()}")
    print(f"Testing healing_potion: {potions.healing_potion()}")


main()
