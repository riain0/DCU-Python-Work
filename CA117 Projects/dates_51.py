import sys


def dates(s):
    s = s.split()
    day = s[0]
    m = s[1]
    y = s[2]
    months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
    }
    new_m = 0
    for k in months:
        v = months.get(k)
        if m == k:
            m = months[k]
    y = y[2:]

    return "{}/{}/{}".format(day, m, y)


def main():
    for s in sys.stdin:
        print(dates(s))


if __name__ == '__main__':
    main()
