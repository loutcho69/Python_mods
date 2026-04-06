from alchemy.grimoire.light_spellbook import light_spell_record


def main() -> None:
    name = "abracadabra"
    test = "Earth , wind and fire"
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing rercord light spell: {light_spell_record(name, test)}")


main()
