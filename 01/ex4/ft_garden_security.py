class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self._name = name
        self._height = height
        self._age = day

    def show(self) -> None:
        print(
            f"{self._name}: {self.get_height()}cm, "
            f"{self.get_age()} days old"
            )

    def grow(self) -> None:
        self._height += 0.8
        self._height = round(self._height, 2)

    def age(self) -> None:
        self._age += 1

    def set_height(self, height_set: float) -> None:
        if height_set >= 0:
            self._height = height_set
            print(f"\nHeight updated: {self._height}cm")
        else:
            print(f"\n{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age_set: int) -> None:
        if age_set >= 0:
            self._age = age_set
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return self._age


def ft_garden_security() -> None:
    rose = Plant("Rose", 70, 5)
    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    rose.show()
    rose.set_height(25)
    rose.set_age(10)
    rose.set_height(-45)
    rose.set_age(-45)
    print("\nCurent state:", end=" ")
    rose.show()


if __name__ == "__main__":
    ft_garden_security()
