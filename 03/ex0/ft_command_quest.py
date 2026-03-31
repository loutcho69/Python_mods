import sys
def script() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    argc = len(sys.argv)
    if argc == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments Received: {argc - 1}")
    for i in range(1, argc):
        print(f"Arguments {i}: {sys.argv[i]}")
    print(f"Total arguments : {argc}")

if __name__ == "__main__":
    script()
