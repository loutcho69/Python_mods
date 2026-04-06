from .light_validator import validate_ingredients

def light_spell_allowed_ingredients() -> list:
    return [ "earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str) ->str:
    if "INVALID" in validate_ingredients(ingredients):
       return f'Spell rejected: {spell_name} ({validate_ingredients(ingredients)})'
    else:
        return f'Spell recorded: {spell_name} ({validate_ingredients(ingredients)})'

