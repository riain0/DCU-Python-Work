import sys
import string
from operator import itemgetter

def is_vowel(l):
    if l in "aeiou":
        return True
    return False


def count_vowels(f):
    vowels = {}
    line = "".join(f)
    line = line.lower()
    line = line.split()
    a = []
    for w in line:
        for l in w:
            if is_vowel(l):
                a.append(l)
                occurences = a.count(l)
                vowels[l] = occurences
    return vowels


def main():
    f = sys.stdin.readlines()
    d = count_vowels(f)
    seen = []
    a = []
    for k in d:
        if k not in seen:
            seen.append(k)
    for i, val in enumerate(seen):
        a.append([seen[i], d[val]])
        a = sorted(a, key=itemgetter(1), reverse=True)
    for p in a:
        print("{} : {:>3d}".format(p[0], p[1]))


if __name__ == '__main__':
    main()
