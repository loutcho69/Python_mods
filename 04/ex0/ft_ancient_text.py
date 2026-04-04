import sys


def parsing() -> None:
    try:
        txt = open(sys.argv[1], "r")
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file: '{sys.argv[1]}'")
        content = txt.read()
        print(content)
        txt.close()
        print(f"File {sys.argv[1]} closed.")
    except FileNotFoundError as e:
        print(f"{e}")
    except IndexError:
        print("Usage: ft_ancient_text.py <file>")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


def main() -> None:
    parsing()


if __name__ == "__main__":
    main()
