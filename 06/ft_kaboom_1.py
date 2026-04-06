
def main() -> None:
    name = "abracadabra"
    test = "earth , air, fire, water"
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        print(f"Testing rercord dark spell: {dark_spell_record(name, test)}")
    except ImportError as e:
        print("=== Kaboom 1 ===")
        print("Access to alchemy/grimoire/dark_spellbook.py directly")
        print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
        print(e)


main()
