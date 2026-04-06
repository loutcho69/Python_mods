from alchemy.grimoire.light_spellbook import light_spell_record

def main() -> None:
    name = "abracadabra"
    test = "earth , air, fire, water"
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing rercord light spell: {light_spell_record(name, test)}")

main()