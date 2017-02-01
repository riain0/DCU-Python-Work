def count_letters(s):
    c = 0
    if not s:
        return 0
    else:
        c += 1
        s = s[1:]
    return c + count_letters(s)
