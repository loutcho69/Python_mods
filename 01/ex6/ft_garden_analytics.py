class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    @staticmethod
    def check_age(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def display(self, name: str) -> None:
            print(f"[statistics for {name}]")
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def show(self) -> None:
        self._stats.increment_show()
        print(f"\n=== {self._name}")
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self, cm: float) -> None:
        self._stats.increment_grow()
        self._height += cm

    def age(self, day: int) -> None:
        self._stats.increment_age()
        self._age += day

    def display_stats(self) -> None:
        self._stats.display(self._name)


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = "has not bloomed yet"

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        print(f"{self._name} {self._bloomed}")

    def bloom(self) -> None:
        self._bloomed = "is blooming beautifully!"


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self._seed = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed}")

    def grow(self, cm: float) -> None:
        super().grow(cm)
        if self._bloomed == "is blooming beautifully!":
            self._seed += int(cm * 1.4)

    def age(self, day: int) -> None:
        self._stats.increment_age()
        self._age += day

    def bloom(self) -> None:
        super().bloom()


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def increment_shade(self) -> None:
            self._shade_calls += 1

        def display(self, name: str) -> None:
            print(f"[statistics for {name}]")
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show, "
                f"{self._shade_calls} shade"
            )

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunck: float,
        shade_long: float,
        shade_wide: float
    ) -> None:
        super().__init__(name, height, age)
        self._stats: Tree.Stats = Tree.Stats()
        self._trunck_diameter = trunck
        self._shade_long = shade_long
        self._shade_wide = shade_wide

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunck_diameter, 1)}cm")

    def produce_shade(self, long: float, wide: float) -> None:
        self._stats.increment_shade()
        print(f"[asking the {self._name.lower()} to produce shade]")
        self._shade_long += long
        self._shade_wide += wide
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._shade_long, 1)}cm long "
            f"and {round(self._shade_wide, 1)}cm wide."
        )


def stat_display(plant: "Plant") -> None:
    plant.display_stats()


def main() -> None:
    print("=== Garden statistics ===")

    print("\n=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")

    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    stat_display(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    stat_display(rose)

    oak = Tree("Oak", 200, 365, 5, 0, 0)
    oak.show()
    stat_display(oak)
    oak.produce_shade(200, 5)
    stat_display(oak)

    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.bloom()
    sunflower.age(20)
    sunflower.grow(30)
    sunflower.show()
    stat_display(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    stat_display(unknown)


if __name__ == "__main__":
    main()
