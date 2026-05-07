import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops: dict[str, Callable[[int, int], int]] = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda a, b: a if a > b else b,
        'min': lambda a, b: a if a < b else b,
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(ops[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    fire_enchant = functools.partial(base_enchantment, 50, 'fire')
    ice_enchant = functools.partial(base_enchantment, 50, 'ice')
    lightning_enchant = functools.partial(base_enchantment, 50, 'lightning')
    return {
        'fire': fire_enchant,
        'ice': ice_enchant,
        'lightning': lightning_enchant,
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fire", "ice", "lightning"]))
    print(dispatch(3.14))
