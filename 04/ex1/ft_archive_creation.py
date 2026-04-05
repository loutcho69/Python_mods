import sys


def file_editor() -> None:
    try:
        txt = open(sys.argv[1], "r")
        print(f"Accessing file: '{sys.argv[1]}'\n---\n")
        content = txt.readlines()
        for line in content:
            line = line.replace("\n", "")
            print(f"{line}")
        print(f"\n---\nFile {sys.argv[1]} closed.\n")
        print("Transform data:\n---\n")
        for line in content:
            line = line.replace("\n", "")
            print(f"{line}#")
        txt.close()
        new_name = input("\n---\nEnter new file name (or empty): ")
        if len(new_name) <= 1:
            sys.stdout.write("Empty file name. \nData not saved.")
            txt.close()
            return
        else:
            sys.stdout.write(f"Saving data to: '{new_name}'\n")
        new = open(new_name, "w")
        txt = open(sys.argv[1], "r")
        content = txt.readlines()
        for line in content:
            line = line.replace("\n", "")
            new.write(f"{line}#\n")
        new.close()
        txt.close()
        sys.stdout.write(f"Data saved in file '{new_name}'\n")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except IndexError:
        print("Usage: ft_ancient_text.py <file>")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    file_editor()


if __name__ == "__main__":
    main()
