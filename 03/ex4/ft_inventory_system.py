import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        parts = arg.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, quantity = parts
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            qty = int(quantity)
            if qty < 0:
                print(f"Error - negative quantity for '{name}'")
                continue
            inventory[name] = qty
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
    return inventory


def display_inventory(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    print(f"Item list: {items}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    for name, qty in inventory.items():
        pct = round(qty / total * 100, 1)
        print(f"Item {name} represents {pct}%")
    most = max(inventory, key=lambda k: inventory[k])
    least = min(inventory, key=lambda k: inventory[k])
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]
    inventory = parse_inventory(args)
    if not inventory:
        print("Error - empty inventory")
        return
    display_inventory(inventory)
    inventory['magic_item'] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
