import re
import sys


def main():
    phone = re.compile("\d{2}\s\d{7}")
    phone2 = re.compile("\d{2}\S\d{7}")
    date1 = re.compile("\d\S\d\S\d{2}")
    date2 = re.compile("\d{2}\S\d{2}\d{2}")
    email = re.compile("(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*")
    date3 = re.compile("\d{2}\s\d{3}\s\d{2}")
    s = sys.stdin.read()
    a_p = phone.findall(s) + phone2.findall(s)
    a_d_1 = date1.findall(s) + date2.findall(s)
    a_e = email.findall(s)
    a_d_2 = date3.findall(s)
    print(date1.findall(s))
    print(date2.findall(s))
    print(a_d_1)
    print(a_p)
    print(a_e)
    print(a_d_2)


if __name__ == '__main__':
    main()
