import sys


def get_roots(a, b, c):
    z = (b ** 2) - (4 * ( a * c))
    if z >= 0:
        r1 = (-b + ((z) ** 0.5)) / (2 * a)
        r2 = (-b - ((z) ** 0.5)) / (2 * a)
        return [r1, r2]
    return None


def main():
    for v in sys.stdin:
        v = v.strip().split()
        a = float(v[0])
        b = float(v[1])
        c = float(v[2])
        r = get_roots(a, b, c)
        if r:
            print("r1 = {}, r2 = {}".format(r[0], r[1]))
        else:
            print(r)


if __name__ == "__main__":
    main()
