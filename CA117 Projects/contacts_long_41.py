import sys

def get_info(f):
    phone_book = {}
    with open(f) as f:
        for line in f:
            line = line.split()
            name = line[0]
            number = line[1]
            email = line[2]
            phone_book[name] = [number, email]
    return phone_book


def main():
    f = sys.argv[1]
    d = get_info(f)
    lines = sys.stdin.readlines()
    for name in lines:
        name = name.strip("\n")
        if name in d:
            print("Phone: {}".format(d[name][0]))
            print("Email: {}".format(d[name][1]))
        else:
            print("No such contact")


if __name__ == "__main__":
    main()
