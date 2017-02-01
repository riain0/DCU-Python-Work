# Sample questions for CA116 semester one exam.
# Questions and solutions updated as of 16/01/2016

# Iterate over the list letters to print L I S T on one line
# list is: ['L', 'I', 'S', 'T'] but do not put this in your function.


def iter_over():
    # +++Your code here+++
    return


# Replace Tuple with LIST
# list is: ['String', 'Dictionary', 'Tuple'] but do not use it in function


def replace():
    # +++Your code here+++
    return


# Print the appropriate element (LIST of this data structure
# list is: [['Tuple', 'int'], ['LIST', 'float'], ['String, 'double']] but do not use in function


def print_apt():
    # +++Your code here+++
    return


# Print the correct dictionary value (DICT)
# dictionary: {'str': 'String', 'int': 'Integer', 'dict': 'DICT',} but don't use in function


def print_cor():
    # +++Your code here+++
    return


# Q3b from CA116 2015/16 Sample Exam
# Encode a given string using a dictionary in the form of a Caesar Cypher
# dictionary: {'a': 'b', 'b': 'c', 'c': 'a'} but don't use in function

def encode():
    # +++Your code here+++
    return


# Iterate over a string but don't print any X's


def iter_over_x():
    # +++Your code here+++
    return


# Use binary search to check whether a list contains LIST or not


def bsearch():
    # +++Your code here+++
    return


def contains():
    # +++Your code here+++
    return


# Create a function that converts a binary string into a decimal string


def bconvert():
    # +++Your code here+++
    return


# Create a function that converts a decimal string into binary, hex or octal dependent on a parameter,
# no need to use A-F for hex


def dconvert():
    # +++Your code here+++
    return


######################################################################################################


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
