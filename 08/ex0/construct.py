import sys
import os


def in_virtualenv() -> bool:
    return sys.prefix != sys.base_prefix


def show_outside():
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("")
    print("To enter the construct, run:")
    print("    python -m venv matrix_env")
    print("    source matrix_env/bin/activate")
    print("")
    print("Then run this program again.")


def show_inside():
    venv_name = os.path.basename(sys.prefix)
    package_path = os.path.join(
        sys.prefix, "lib",
        f"python{sys.version_info.major}.{sys.version_info.minor}",
        "site-packages"
    )
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {sys.prefix}")
    print("")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("")
    print(f"Package installation path: {package_path}")


if __name__ == "__main__":
    if in_virtualenv():
        show_inside()
    else:
        show_outside()
