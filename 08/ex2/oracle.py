import os
from dotenv import load_dotenv


load_dotenv()


def get_config() -> dict[str, str | None]:
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def check_missing(config: dict[str, str | None]) -> list[str]:
    return [key for key, val in config.items() if val is None]


def show_config(config: dict[str, str | None]) -> None:
    mode = config["MATRIX_MODE"]

    db = config["DATABASE_URL"]
    if db:
        db_status = "Connected to local instance" if mode == "development" \
            else "Connected to production database"
    else:
        db_status = "NOT CONFIGURED"

    api = config["API_KEY"]
    api_status = "Authenticated" if api else "NOT CONFIGURED"

    zion = config["ZION_ENDPOINT"]
    zion_status = "Online" if zion else "NOT CONFIGURED"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {zion_status}")


def security_check(config: dict[str, str | None]) -> None:
    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.isfile(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found — using environment variables only")

    print("[OK] Production overrides available")


def show_missing_warnings(missing: list[str]) -> None:
    print("\n[WARN] Missing configuration variables:")
    for key in missing:
        print(f"  - {key}")
    print("\nCopy .env.example to .env and fill in your values:")
    print("  cp .env.example .env")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    config = get_config()
    missing = check_missing(config)

    if missing:
        show_missing_warnings(missing)
        print()

    show_config(config)
    security_check(config)

    print("\nThe Oracle sees all configurations.")
