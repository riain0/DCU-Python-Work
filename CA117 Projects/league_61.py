import sys
from operator import itemgetter

def get_score(s):
    s = s.strip().split()
    club = " ".join(s[:-5])
    scores = s[-5:]
    total = 0
    test = ""

    for n in scores:
        test += n
    if test.isdigit():
        for c in test:
            try:
                total += int(c)
            except ValueError:
                pass
    if total:
        return [club, total]


def main():
    a = []
    for s in sys.stdin:
        scores = get_score(s)
        if scores:
            a.append(scores)
            a = sorted(a, key=itemgetter(1), reverse=True)
    for v in a:
        print("{} {} points".format(v[0], v[1]))


if __name__ == "__main__":
    main()
