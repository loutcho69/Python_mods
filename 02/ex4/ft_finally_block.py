class PlantError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


def water_plant(plant_name) -> None:

    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water:'{plant_name}'")


def test_watering_system() -> None:
    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def main():
    print("=== Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors")


if __name__ == "__main__":
    main()
