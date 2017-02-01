import sys
import string


def setup(f):
    words = {}
    line = "".join(f)
    line = line.lower()
    line = line.strip("\n")
    for p in string.punctuation:
        if p != "'":
            line = line.replace(p, "")
    line = line.split()
    for w in line:
        if len(w) > 3:
            occurences = line.count(w)
            if occurences >= 3:
                words[w] = occurences
    return words


def main():
    f = sys.stdin.readlines()
    d = setup(f)
    a = []
    for w in d:
        a.append(w)
        a = sorted(a)
    for sw in a:
        print(sw, ":", d[sw])



if __name__ == '__main__':
    main()
