class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_intro() -> None:
    rose = Plant("Rose", 25, 30)
    print("=== Welcome to My Garden ===")
    print(f"Plant: {rose.name}")
    print(f"Heignt: {rose.height}cm")
    print(f"Age: {rose.age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
