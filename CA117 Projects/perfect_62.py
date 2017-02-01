import sys


def sumFac(n):
    a = []
    for i in range(1, n):
        if not n % i:
            a.append(i)
    return sum(a)


def isPerfect(n):
    sumf = sumFac(n)
    if n - sumf == 0:
        return True
    return False


def main():
    for n in sys.stdin:
        n = n.strip()
        n = int(n)
        print(isPerfect(n))


if __name__ == "__main__":
    main()
