import random


def almemist() -> None:
    print("=== Game Data Alchemist ===")
    players = [
        "bob", "Alice", "dylan", "Charlie",
        "Emma", "Gregory", "john", "kevin", "Liam"
     ]
    print(f"Initial list of players: {players}")
    new_list = []
    for player in players:
        if player == player.capitalize():
            new_list.append(player)
    for i in range(len(players)):
        players[i] = players[i].capitalize()
    print(f"New list with all names capitalized: {players}")
    print(f"New list of capitalized names only: {new_list}")
    inventory = {}
    for player in players:
        inventory[player] = random.randint(0, 1000)
    print(f"Score dict: {inventory}")
    average = sum(inventory.values()) / len(inventory)
    print(f"Score average: {round(average, 2)}")
    hight_score = {}
    for player in inventory:
        if inventory[player] > average:
            hight_score[player] = inventory[player]
    print(f"High scores: {hight_score}")


if __name__ == "__main__":
    almemist()
