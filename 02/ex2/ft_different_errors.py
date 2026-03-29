def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("test.txt")
    elif operation_number == 3:
        "temperature" + 25
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    try:
        print("Testing operation 0...")
        garden_operations(0)
    except ValueError as e:
        print(f"ValueError: {e}")

    try:
        print("Testing operation 1...")
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")

    try:
        print("Testing operation 2...")
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    try:
        print("Testing operation 3...")
        garden_operations(3)
    except TypeError as e:
        print(f"TypeError: {e}")
    print("Testing operation 4...")
    garden_operations(25)
    print("Operation completed successfully")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
