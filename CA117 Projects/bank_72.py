class BankAccount(object):

    def __init__(self, bal=0):
        self.bal = bal


    def __str__(self):
        return "Your balance is: {:.2f} euro".format(self.bal)


    def deposit(self, m=0):
        self.bal += m
        print(BankAccount.__str__(self))


    def withdraw(self, m=0):
        if self.bal >= m:
            self.bal -= m
            print(BankAccount.__str__(self))
        else:
            print("Insufficient funds available")
