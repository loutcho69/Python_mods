class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = "has not bloomed yet"

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        print(f"{self._name} {self._bloomed}")

    def bloom(self) -> None:
        self._bloomed = "is blooming beautifully!"
        print(f"[asking the {self._name} to bloom]")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunck: int,
        shade_long: int,
        shade_wide: int
    ) -> None:
        super().__init__(name, height, age)
        self._trunck_diameter = trunck
        self._shade_long = shade_long
        self._shade_wide = shade_wide

    def show(self) -> None:
        super().show()
        print(f"Trunck diameter: {round(self._trunck_diameter, 1)}cm")

    def produce_shade(self, long: int, wide: int) -> None:
        print(f"[asking the {self._name} to produce shade]")
        self._shade_long += long
        self._shade_wide += wide
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._shade_long, 1)}cm "
            f"and {round(self._shade_wide, 1)}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest: str,
        nutri: int
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest
        self._nutritional_value = nutri

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self, day: int) -> None:
        self._age = day
        self._nutritional_value += day

    def grow(self, height: int) -> None:
        self._height = height

    def growing(self, day: int, height: int) -> None:
        self.age(day + self._age)
        self.grow(height + self._height)
        print(f"[make the {self._name} grow and age for {day} days]")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 5, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak = Tree("Oak", 450, 365, 30, 170, 55)
    oak.show()
    oak.produce_shade(30, 5)
    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    tomato.show()
    tomato.growing(20, 25)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
