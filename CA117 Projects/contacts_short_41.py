import sys

def get_info(f):
    phone_book = {}
    with open(f) as f:
        for line in f:
            line = line.split()
            name = line[0]
            number = line[1]
            phone_book[name] = number
    return phone_book


def main():
    f = sys.argv[1]
    d = get_info(f)
    lines = sys.stdin.readlines()
    for name in lines:
        name = name.strip("\n")
        if name in d:
            print("Phone: {}".format(d[name]))
        else:
            print("No such contact")


if __name__ == "__main__":
    main()
