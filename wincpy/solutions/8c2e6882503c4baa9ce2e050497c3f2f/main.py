import argparse
import sys

# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Your code here
def main():
    text = sys.stdin.read()
    if len(sys.argv) == 1:
        sys.stderr.write("0")
        sys.stdout.write(text)
    else:
        filter_char = sys.argv[1]
        sys.stdout.write(text.replace(filter_char, ""))
        sys.stderr.write(str(text.count(filter_char)))


if __name__ == "__main__":
    main()
