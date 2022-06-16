from subprocess import run
from pathlib import Path
import sys


HERE = Path(__file__)

def main():
    args = [HERE.parent / "bin" / "uncrustify"]
    args.extend(sys.argv[1:])

    sys.exit(run(args).returncode)

if __name__ == "__main__":
    main()
