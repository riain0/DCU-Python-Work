def count_char(s, c):
    count = 0
    for ch in s:
        if ch == c:
            count += 1
        return count
    return count_char(c, s)
