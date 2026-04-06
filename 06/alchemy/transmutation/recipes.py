from elements import create_fire
from alchemy.elements import create_air
from alchemy import potions


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: brew "
        f"'{create_air()}' and '{potions.strenght_potion()}'"
        f" mixed with '{create_fire()}'"
    )
