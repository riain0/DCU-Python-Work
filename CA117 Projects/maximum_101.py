def maximum(a):
    if len(a) == 0:
        return None

    if len(a) == 1:
        return a[0]

    if len(a) == 2:
        if a[0] > a[1]:
            return a[0]
        return a[1]

    if a[0] > a[1]:
        a.remove(a[1])

    if a[0] <= a[1]:
        a.remove(a[0])

    return maximum(a)


def main():
    max = None
    print(maximum([6,5,1,3,4]))
    print(maximum([6,5,11,3,4]))
    print(maximum([6,15,11,13,14]))
    print(maximum([6,15,11,13,4]))

if __name__ == '__main__':
    main()
