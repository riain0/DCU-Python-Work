import sys


def get_score(i, s):
    tile_values = {
    'a':1,'f':4,
    'k':5,'p':3,'u':1,'z':10,
    'b':3, 'c':3, 'd':2, 'e':1,
    'g':2, 'h':4, 'i':1, 'j':8,
    'l':1, 'm':3, 'n':1, 'o':1,
    'q':10, 'r':1, 's':1, 't':1,
    'v':4, 'w':4, 'x':8, 'y':4,
    }
    s = s.strip("\n")
    a = []
    l = []
    score = 0
    for c in i:
        if c in s and len(i) == len(s) + 1:
            score += tile_values[c]
            a.append([s, score])
            l = a[-1]
    return l


def main():
    i = sys.argv[1]
    for s in sys.stdin:
        sc = get_score(i, s)
        if sc:
            print("{}: {}".format(sc[0], sc[1]))


if __name__ == "__main__":
        main()
