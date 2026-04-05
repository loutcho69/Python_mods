import sys


def file_editor() -> None:
    try:
        txt = open(sys.argv[1], "r")
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file: '{sys.argv[1]}'\n---\n")
        content = txt.readlines()
        for line in content:
            line = line.replace("\n", "")
            print(f"{line}#")
        txt.close()
        print(f"\n---\nFile {sys.argv[1]} closed.\n")
        print("Transform data:\n---\n")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_name = sys.stdin.readline()
        print(len(new_name))
        if len(new_name) <= 1:
            sys.stdout.write("Empty file name. \nData not saved.")
            txt.close()
            return
        new = open(new_name, "w")
        txt = open(sys.argv[1], "r")
        content = txt.readlines()
        for line in content:
            line = line.replace("\n", "")
            new.write(f"{line}#\n")
        new.close()
        txt.close()
        sys.stdout.write(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as e:
        sys.stdout.write(f"[STDERR] {e}")
    except IndexError:
        sys.stdout.write("[STDERR] Usage: ft_ancient_text.py <file>")
    except PermissionError as e:
        sys.stdout.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}")


def main() -> None:
    file_editor()


if __name__ == "__main__":
    main()
