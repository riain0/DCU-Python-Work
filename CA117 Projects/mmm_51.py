import sys


def get_median(a):
    if not len(a) % 2:
        return (a[(len(a) // 2) - 1] + a[len(a) // 2]) / 2
    return len(a) // 2


def get_mode(a):
    count = 0
    for n in a:
        if a.count(n) > count:
            count = a.count(n)
            mode = n
    return mode


def get_mean(a):
    total = 0
    for n in a:
        total += n
    return total / len(a)


def main():
    a = []
    for n in sys.stdin:
        n = n.strip()
        n = int(n)
        a.append(n)
    print("Mean: {:.1f}".format(get_mean(a)))
    print("Mode: {:.1f}".format(get_mode(a)))
    print("Median: {:.1f}".format(get_median(a)))



if __name__ == "__main__":
    main()
