import sys
import importlib.util
import importlib.metadata


REQUIRED = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies() -> bool:
    print("Checking dependencies:")
    all_ok = True
    for package, description in REQUIRED.items():
        spec = importlib.util.find_spec(package)
        if spec is None:
            print(f"[MISSING] {package} - {description}")
            all_ok = False
        else:
            version = importlib.metadata.version(package)
            print(f"[OK] {package} ({version}) - {description}")
    return all_ok


def show_install_instructions() -> None:
    print("\nDependencies are missing. Install them with:")
    print("\n  pip:")
    print("    pip install -r requirements.txt")
    print("\n  Poetry:")
    print("    poetry install")
    sys.exit(1)


def run_analysis() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    rng = np.random.default_rng(42)
    data = {
        "signal": rng.normal(loc=0.0, scale=1.0, size=1000),
        "noise": rng.uniform(low=-0.5, high=0.5, size=1000),
        "timestamp": np.arange(1000),
    }
    df = pd.DataFrame(data)
    df["combined"] = df["signal"] + df["noise"]

    print("Generating visualization...")
    fig, axes = plt.subplots(2, 1, figsize=(10, 6))

    axes[0].plot(df["timestamp"][:100], df["signal"][:100], color="green",
                 linewidth=0.8, label="Signal")
    axes[0].plot(df["timestamp"][:100], df["combined"][:100], color="red",
                 linewidth=0.8, alpha=0.7, label="Signal + Noise")
    axes[0].set_title("Matrix Signal Analysis")
    axes[0].set_xlabel("Timestamp")
    axes[0].set_ylabel("Value")
    axes[0].legend()

    axes[1].hist(df["combined"], bins=40, color="green", edgecolor="black",
                 alpha=0.7)
    axes[1].set_title("Distribution of Combined Signal")
    axes[1].set_xlabel("Value")
    axes[1].set_ylabel("Frequency")

    plt.tight_layout()
    output = "matrix_analysis.png"
    plt.savefig(output)
    plt.close()

    print("\nAnalysis complete!")
    print(f"Results saved to: {output}")


def show_pip_vs_poetry() -> None:
    print("\n--- pip vs Poetry ---")
    print("pip            : installs packages globally or in active venv")
    print("                 uses requirements.txt to list dependencies")
    print("Poetry         : manages venv automatically + locks exact versions")
    print("                 uses pyproject.toml + poetry.lock")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    ok = check_dependencies()
    if not ok:
        show_install_instructions()

    show_pip_vs_poetry()
    run_analysis()
