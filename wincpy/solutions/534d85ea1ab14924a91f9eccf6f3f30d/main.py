# Do not modify these lines
__winc_id__ = "534d85ea1ab14924a91f9eccf6f3f30d"
__human_name__ = "errors"


# Your own code for testing your functions here
def main():
    pass


"""Change the three functions below from Look Before You Leap (LBYL) to Easier
to Ask for Forgiveness than Permission (EAFP)"""


# Returns the addition of x and y if it's defined, otherwise returns 0
def add(x, y):
    try:
        return x + y
    except TypeError:
        return 0


# Returns the contents of the file at 'filename', or an empty string if the
# file does not exist
def read_file(filename):
    try:
        return open(filename, "r").read()
    except FileNotFoundError:
        return ""


# Returns item at `index` from list `l` if possible, otherwise returns None
def get_item_from_list(l, index):
    try:
        return l[index]
    except IndexError:
        return None


if __name__ == "__main__":
    main()
