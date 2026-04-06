
def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    spellbook = light_spell_allowed_ingredients()
    for i in spellbook:
        if i not in ingredients:
            return f'{ingredients} - INVALID'
    return f'{ingredients} - VALID'
