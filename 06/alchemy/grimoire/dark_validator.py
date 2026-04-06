from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    spellbook = dark_spell_allowed_ingredients()
    for i in spellbook:
        if i in ingredients:
            return f'{ingredients} - VALID'
    return f'{ingredients} - INVALID'
