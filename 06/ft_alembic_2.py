import alchemy


def main() -> None:
    print("=== Alembic 2 ===\n")
    print("Accessing alchemy/elements.py using 'import ...' structure\n")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")


main()
