class GardenError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self):
        super().__init__("the tomato plant is wilting!")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank!")


def check_water() -> None:
    raise WaterError()


def check_plant() -> None:
    raise PlantError()


def test_erorrs() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_erorrs()
