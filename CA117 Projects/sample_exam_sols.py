# Q3
s = "This is an example sentence"

n = list(range(15))

# Part i
v_count = len([v for v in s.lower() if v in "aeiou"])
print(v_count)

# Part ii
q = [m for m in n if not m % 3]
print(q)

# Part iii
r = [0 if not m % 5 else m for m in n]
print(r)

# Q4

def arithmetic(p, q, r=3, s=5):
    return r - p + q + s

# Q5

dates = r'\b(?:0[1-9]|[1-2]\d|3[0-1])/(?:0[1-9]|1[0-2])/(?:\d\d)\b'

# Q6

class BankAccount(object):

    NEXT_ACCOUNT_NUMBER = 16555232

    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = self.NEXT_ACCOUNT_NUMBER
        self.NEXT_ACCOUNT_NUMBER += 1

    def lodge(self, amount):
        self.balance += amount

class CurrentAccount(BankAccount):

    OVERDRAFT = 0

    def __init__(self):
        super().__init__()

    def withdraw(self, amount):
        if (self.balance + self.OVERDRAFT) - amount < 0:
            print("Insufficient funds available")
            return
        self.balance -= amount

class SavingsAccount(BankAccount):

    INTEREST_RATE = 1.01

    def __init__(self):
        super().__init__()

    def apply_interest(self):
        self.balance *= self.INTEREST_RATE

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds available")
            return
        self.balance -= amount

# Q7

def count_char(s, c):
    if s == '':
        return 0
    else:
        is_c = int(s[0] == c)  # 1 if True, 0 if False
        return is_c + count_char(s[1:], c)

# Q8 i

def partition(A, p, r):
    q = j = p
    while j < r:
        if A[j] <= A[r]:
            A[q], A[j] = A[j], A[q]
            q += 1
        j += 1
        A[q], A[r] = A[r], A[q]
        return q
A = [10, 20, 59, 83, 18, 47, 44, 96, 16, 38]
partition(A, 0, len(A)-1)
print(A)

A = [10, 20, 18, 16, 38, 47, 44, 96, 83, 59]

# Q8 ii

def quicksort(A, p, r):
    if r <= p:
        return
    q = partition(A, p, r)
    quicksort(A, p, q-1)
    quicksort(A, q+1, r)

# Q9a

class House(object):

    def __init__(self, address, value, bedrooms, garden):
        self._address = address
        self._value = value
        self._bedrooms = bedrooms
        self._garden = garden

    def __str__(self):
        return "{}\n{}\n{}\n{}".format(self._address, self._value, self._bedrooms, self._garden)

    def getValueRange(self):
        value = int(self._value)
        if value < 200000:
            return "< 200000"
        elif 200000 <= value < 349999:
            return "200000-349999"
        elif 350000 <= value < 499999:
            return "350000-499999"
        else:
            return ">= 500000"

    def isComparableValue(self, other):
        if self.getValueRange() == other.getValueRange():
            return True
        return False

# Q9b

import sys

details = [k.strip() for k in sys.stdin]

house1 = details[0].split(",")
house2 = details[1].split(",")

h1 = House(house1[0], house1[1], house1[2], house1[3])
h2 = House(house2[0], house2[1], house2[2], house2[3])

print(h1.isComparableValue(h2))

# Q10a

class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return "Name: {}\nPhone: {}\nEmail: {}".format(self.name, self.phone, self.email)

class ContactList(object):

    def __init__(self):
        self.clist = {}

    def add(self, contact):
        if contact.name not in clist:
            self.clist[contact.name] = contact
        else:
            print("Contact already present")

    def display(self, name):
