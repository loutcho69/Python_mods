from .grimoire import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    from .grimoire import (dark_spell_allowed_ingredients)
    spellbook = dark_spell_allowed_ingredients()
    for i in spellbook:
        if i not in ingredients:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"

