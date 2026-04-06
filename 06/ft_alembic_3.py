from alchemy import create_air


def main() -> None:
    print("=== Alembic 3 ===\n")
    print("Accessing alchemy/elements.py using"
          "'from ... import ...' structure\n")
    print(f"Testing create_air: {create_air()}")


main()
