from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str],
) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int,
) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str],
) -> Callable[[str, int], str]:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(
    spells: list[Callable[[str, int], str]],
) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    short1 = result[0].split(" for ")[0]
    short2 = "Heals Dragon"
    print(f"Combined spell result: {short1}, {short2}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original_power = 10
    amplified_result = mega_fireball("Dragon", original_power)
    amplified_power = original_power * 3
    print(f"Original: {original_power}, Amplified: {amplified_power}")

    print("\nTesting conditional caster...")
    high_power_only = conditional_caster(
        lambda t, p: p >= 20,
        fireball,
    )
    print(high_power_only("Goblin", 25))
    print(high_power_only("Goblin", 5))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    results = sequence("Dragon", 10)
    for r in results:
        print(r)

    print("\nCallable demo — callable() checks:")
    print(f"fireball is callable: {callable(fireball)}")
    print(f"42 is callable: {callable(42)}")
