import sys


def parsing() -> None:
    try:
        txt = open(sys.argv[1], "r")
        print(f"Accessing file: '{sys.argv[1]}'\n---\n")
        content = txt.read()
        print(content)
        txt.close()
        print(f"\n---\nFile {sys.argv[1]} closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except IndexError:
        print("Usage: ft_ancient_text.py <file>")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    parsing()


if __name__ == "__main__":
    main()
