def minimum(a):
    if len(a) == 0:
        return None

    if len(a) == 1:
        return a[0]

    if len(a) == 2:
        if a[0] < a[1]:
            return a[0]
        return a[1]

    if a[0] < a[1]:
        a.remove(a[1])

    if a[0] >= a[1]:
        a.remove(a[0])

    return minimum(a)
