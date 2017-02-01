def a():
	l = []
	for n in range(1, 31):
		l.append(n)
	return l


def multiples_3():
	l = a()
	return [n for n in l if not n % 3]


def multiples_4():
	l = a()
	return [n for n in l if not n % 4]


def mults_3_sqrd():
	l = multiples_3()
	return [n**2 for n in l]


def mults_4_doub():
	l = multiples_4()
	return [n*2 for n in l]


def mults_3_or_4():
	l = a()
	return [n for n in l if((not n % 3) or (not n % 4))]


def mults_3_and_4():
	l = a()
	return [n for n in l if((not n % 3) and (not n % 4))]


def extract_mults_3():
	l = a()
	a_3 = multiples_3()
	return [n if not n in a_3 else 'X' for n in l]


def main():
	print("Multiples of 3: {}".format(multiples_3()))
	print("Multiples of 3 squared: {}".format(mults_3_sqrd()))
	print("Multiples of 4 doubled: {}".format(mults_4_doub()))
	print("Multiples of 3 or 4: {}".format(mults_3_or_4()))
	print("Multiples of 3 and 4: {}".format(mults_3_and_4()))
	print("Multiples of 3 replaced: {}".format(extract_mults_3()))


if __name__ == "__main__":
	main()