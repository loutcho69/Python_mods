class Plant:
    def __init__(self, name: str, height, day):
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

def ft_garden_data() -> None:
    plants = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
    cms = [25, 200, 5, 80, 15]
    days = [30, 365, 90, 45, 120]
    print("=== Plant Factory Output ===")
    for i in range(0, 5):
        current = Plant(plants[i], cms[i], days[i])
        print("Created:", end= " ")
        current.show()

def main():
    ft_garden_data()

if __name__ == "__main__":
    main()
