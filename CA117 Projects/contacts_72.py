class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


    def __str__(self):
        return "{} {} {}".format(self.name, self.phone, self.email)

class ContactList(object):

    def __init__(self, d={}):
        self.d = d


    def add_contact(self, c):
        self.d[c.name] = c.phone, c.email


    def del_contact(self, c):
        if c.name in self.d:
            del self.d[c.name]


    def get_contact(self, c):
        if c.name in self.d:
            return "{} {} {}".format(c.name, c.phone, c.email)
        else:
            print("{} : No such contact".format(c.name))


    def __str__(self):
        
