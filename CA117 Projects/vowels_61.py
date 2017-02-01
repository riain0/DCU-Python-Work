import sys
test = False

def vowels(s):
    vow = list("aeiou")
    seq = []
    for c in s.lower():
        if c in vow:
            seq.append(c)
    if seq == vow:
        return s


def main():
    for s in sys.stdin:
        if vowels(s):
            print(s.strip())


if __name__ == "__main__":
        main()
