class Student(object):

    def __init__(self, surname, forename, sid, modlist=[]):
        self.sid = sid
        self.surname = surname
        self.forename = forename
        self.modlist = modlist


    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)


    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)


    def print_details(self):
        print("ID: {}".format(self.sid))
        print("Surname: {}".format(self.surname))
        print("Forename: {}".format(self.forename))
        print("Modules: {} ".format(" ".join(self.modlist)))
