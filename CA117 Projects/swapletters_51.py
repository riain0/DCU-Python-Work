import sys


def swap(s):
    return("".join([(s[i:i + 2])[::-1] for i in range(0, len(s),2)]))


def main():
    s = sys.argv[1]
    print(swap(s))


if __name__ == "__main__":
    main()
