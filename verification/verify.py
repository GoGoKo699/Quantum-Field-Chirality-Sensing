"""Run the project's finite matrix and detector checks."""

import subprocess
import sys
from pathlib import Path


def main():
    for name in ("verify_protocol.py", "verify_two_exposures.py", "verify_robustness.py"):
        subprocess.run([sys.executable, str(Path(__file__).with_name(name))], check=True)


if __name__ == "__main__":
    main()
