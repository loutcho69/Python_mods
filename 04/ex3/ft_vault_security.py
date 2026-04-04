import sys

def secure_archive(fl: str, action: str, content: str = "") -> tuple[bool, str]:
    try:
        print("=== Cyber Archives Security ===")
        if action == 'w' and content == "":
            return False, "Error - no content to write"
        with open(fl, action) as f:
            res = []
            if action == 'r':
                res = f.read()
            if action == 'w' and content != "":
                res = f.write(content)
        return True, res
    except ValueError as e:
        return False ,sys.stdout.write(f"[STDERR] {e}")
    except FileNotFoundError as e:
        return False ,sys.stdout.write(f"[STDERR] {e}")
    except IndexError:
        return False ,sys.stdout.write("[STDERR] Usage: ft_ancient_text.py <file>")
    except PermissionError as e:
        return False ,sys.stdout.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}")

secure_archive('test.txt', 'w')