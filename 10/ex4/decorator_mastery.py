import time
import functools
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    """Decorator factory: validates the first non-self int argument (power)."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power: Any = None
            for arg in args:
                if isinstance(arg, int):
                    power = arg
                    break
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c == ' ' for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball_cast() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball_cast()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def always_fails() -> str:
        raise RuntimeError("Spell unstable")

    print(always_fails())

    _call_count = [0]

    @retry_spell(max_attempts=3)
    def eventually_works() -> str:
        _call_count[0] += 1
        if _call_count[0] < 3:
            raise RuntimeError("Not yet")
        return "Waaaaaaagh spelled !"

    print(eventually_works())
    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X2"))
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Spark"))
