def ft_count_harvest_recursive(day: int, days: int) -> None:
    if day <= days:
        print(f"Day {day}")
    if day <= days:
        ft_count_harvest_recursive(day + 1, days)


def main() -> None:
    days = int(input("Days until harvest: "))
    ft_count_harvest_recursive(1, days)
    print("Harvest time")
