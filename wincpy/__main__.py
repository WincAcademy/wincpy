import sys

from wincpy.main import main


def console_entry() -> None:
    main(sys.stdout, sys.stderr)


if __name__ == '__main__':
    main(sys.stdout, sys.stderr)
