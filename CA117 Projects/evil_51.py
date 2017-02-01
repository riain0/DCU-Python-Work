import sys

def evil(s):
    ev = list("evil")
    seq = []
    a = []
    for c in s.lower():
        if c in ev:
            seq.append(c)
    if seq == ev:
        a.append(s)
        for l in a:
            print(l.strip())


def main():
    for s in sys.stdin:
        evil(s)


if __name__ == "__main__":
    main()
