import alchemy

def main() -> None:
    print("=== Alembic 4 ===\n")
    print("Accessing the alchemy module using 'import alchemy'\n")
    try:
        print(f"Testing create_air: {alchemy.create_air()}")
        print(f"Testing create_earth: {alchemy.create_earth()}")
    except AttributeError as e:
        print(f"Testing create_earth: ERROR --> {e}")

main()