import random


def set_achivements(achievements: set[str]) -> set[str]:
    nb = random.randint(1, len(achievements))
    return set(random.sample(list(achievements), nb))


def gen_player_achievements() -> None:
    achievements = {
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable', 'First Steps',
        'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer'
    }
    alice = ("Alice", set_achivements(achievements))
    bob = ("Bob", set_achivements(achievements))
    charlie = ("Charlie", set_achivements(achievements))
    dylan = ("Dylan", set_achivements(achievements))
    players = [alice, bob, charlie, dylan]
    common = set(alice[1])
    for i in players:
        print(f"Player {i[0]}: {i[1]} ")
        common &= i[1]
    print(f"\nAll distinct achivements: {set(achievements)}\n")
    print(f"Common achivements: {common}\n")
    for i in players:
        unique = set()
        for p in players:
            unique |= i[1]
        print(f"Only {i[0]} has: {unique} \n")
    for i in players:
        base = set(achievements)
        res = base - i[1]
        print(f"{i[0]} is missing: {res} \n")


def main() -> None:
    print("=== Achievement Tracker System ===")
    gen_player_achievements()


if __name__ == "__main__":
    main()
