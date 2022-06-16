from subprocess import run
from pathlib import Path
import platform
import sys



HERE = Path(__file__)

def main():
    if platform.system() == "Windows":
        args = [HERE.parent / "uncrustify.exe"]
    else:
        args = [HERE.parent / "bin" / "uncrustify"]
    args.extend(sys.argv[1:])

    sys.exit(run(args).returncode)

if __name__ == "__main__":
    main()
