from elements import create_fire
from alchemy import potions, create_air

def lead_to_gold() ->str:
    return (
    "Recipe transmuting Lead to Gold: brew "
    f"'{create_air()}' and '{potions.strenght_potion()}"
    f" mixed with '{create_fire()}'"
)