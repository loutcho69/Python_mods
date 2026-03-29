class Plant:
    def __init__(self, name, height, day):
        self.name = name
        self.height = height
        self.day = day

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.day} days old")

    def grow(self) -> None:
        self.height += 0.8
        self.height = round(self.height, 2)

    def age(self) -> None:
        self.day += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30)
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
