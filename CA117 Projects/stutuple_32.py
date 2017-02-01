from collections import namedtuple

Student = namedtuple("Student", ["firstname", "surname", "id"])


def show_student(s):
	print("{:s} {:3s}".format("First name:", s.firstname))
	print("{:>11s} {:<3s}".format("Surname:", s.surname))
	print("{:>11s} {:<3d}".format("ID:", s.id))

