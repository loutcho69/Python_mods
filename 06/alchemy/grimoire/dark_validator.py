def validate_ingredients(ingredients: str) -> str:
    from .dark_spellbook import dark_spell_allowed_ingredients
    spellbook = dark_spell_allowed_ingredients()
    for i in spellbook:
        if i in ingredients.lower():
            return f'{ingredients} - VALID'
    return f'{ingredients} - INVALID'
