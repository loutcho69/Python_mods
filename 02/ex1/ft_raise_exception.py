def input_temperature(temp_str: str) -> int:
    res = int(temp_str)
    if res < 0:
        raise ValueError (f"{res}°C is too cold for plants (min 0°C)")
    if res > 40:
        raise ValueError (f"{res}°C is too hot for plants (max 40°C)")
    return int(temp_str)

def test_temperature() -> None:
    print("=== Garden Temperature Checker")
    print("Input data is: '25'")
    print(f"Temperature  is now {input_temperature('25')}°C")
    try:
        print("Input data is: 'abc'")
        input_temperature("abc")
    except ValueError as e:
        print(f"Cought input_temperature error: {e}")
    try:
        print("Input data is: '100'")
        input_temperature("100")
    except ValueError as e:
        print(f"Cought input_temperature error: {e}")
    try: 
        print("Input data is: '-50'")
        input_temperature("-50")
    except ValueError as e:
        print(f"Cought input_temperature error: {e}")
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()