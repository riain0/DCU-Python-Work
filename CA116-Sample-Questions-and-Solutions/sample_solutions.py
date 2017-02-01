# Iterate over the list letters to print L I S T on one line
# list is: ['L', 'I', 'S', 'T'] but do not put this in your function.


def iter_over(a):
    s = ''
    i = 0
    while i < len(a):
        s += a[i] + ' '
        i += 1
    return s


# Replace Tuple with LIST
# list is: ['String', 'Dictionary', 'Tuple'] but do not use it in function


def replace(a):
    a.pop()
    a.append('LIST')
    return a


# Print the appropriate element (LIST of this data structure
# list is: [['Tuple', 'int'], ['LIST', 'float'], ['String, 'double']] but do not use in function


def print_apt(a):
    ls = a[1]
    return ls[0]


# Print the correct dictionary value (DICT)
# dictionary: {'str': 'String', 'int': 'Integer', 'dict': 'DICT',} but don't use in function


def print_cor(d):
    val = d.get('dict')
    return val


# Q3b from CA116 2015/16 Sample Exam
# Encode a given string using a dictionary in the form of a Caesar Cypher
# dictionary: {'a': 'b', 'b': 'c', 'c': 'a'} but don't use in function

def encode(d, s):
    new_s = ''
    i = 0
    for char in s:
        if char in d:
            new_s += d[s[i]]
        i += 1
    return new_s


# Iterate over a string but don't print any X's


def iter_over_x(s):
    new_s = ''
    for char in s:
        if char == 'X':
            pass
        else:
            new_s += char
    return new_s


# Use binary search to check whether a list contains LIST or not


def bsearch(a, q):
    low = 0
    high = len(a)
    while low < high:
        mid = (low + high) / 2
        if a[mid] < q:
            low = mid + 1
        else:
            high = mid
    return low


def contains(a):
    q = 'LIST'
    p = bsearch(a, q)
    return p < len(a) and a[p] == q


# Create a function that converts a binary string into a decimal string


def bconvert(s):
    power = len(s) - 1
    output = 0
    for v in s:
        output += int(v) * (2 ** power)
        power -= 1
    return output


# Create a function that converts a decimal string into binary, hex or octal dependent on a parameter,
# no need to use A-F for hex


def dconvert(s, b):
    output = ''
    d = 1
    while (b ** d) <= s:
        d += 1
    i = 0
    while i < d:
        power = (b ** (d - i - 1))
        output += str(s / power)
        s %= power
        i += 1
    return output


# Test function's from Google PyQuick programme.


def test(got, expected):
    if got == expected:
        prefix = 'Correct'
    else:
        prefix = 'Incorrect'
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    print 'Iter Over'
    test(iter_over(['L', 'I', 'S', 'T']), 'L I S T ')
    print 'Replace'
    test(replace(['String', 'Dictionary', 'Tuple']), ['String', 'Dictionary', 'LIST'])
    print 'Print apt'
    test(print_apt([['Tuple', 'int'], ['LIST', 'float'], ['String', 'double']]), 'LIST')
    print 'Print cor'
    test(print_cor({'str': 'String', 'int': 'Integer', 'dict': 'DICT'}), 'DICT')
    print 'Encode'
    test(encode({'a': 'b', 'b': 'c', 'c': 'a'}, 'cab'), 'abc')
    test(encode({'a': 'b', 'b': 'c', 'c': 'a'}, 'abc'), 'bca')
    test(encode({'a': 'b', 'b': 'c', 'c': 'a'}, 'cba'), 'acb')
    print 'Iter over X'
    test(iter_over_x('XXLIXSXTXX'), 'LIST')
    test(iter_over_x('XXLIST'), 'LIST')
    print 'Contains'
    test(contains(['LIST', 'int', 'string']), True)
    test(contains(['list', 'LiST', 'lIST']), False)
    print 'Binary to decimal'
    test(bconvert('00000101'), 5)
    test(bconvert('111'), 7)
    print 'Decimal to base X'
    test(dconvert(12345, 10), '12345')
    test(dconvert(455, 16), '1127')
    test(dconvert(5, 2), '101')
    test(dconvert(120, 8), '170')


if __name__ == '__main__':
    main()
