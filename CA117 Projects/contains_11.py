import sys

def contains(chars, s):
	for char in chars:
		if char in s:
			s = s.replace(char, "")
		else:
			return False
	return True

def main():
	st = sys.argv[1]
	stt = sys.argv[2]
	print(contains(st, stt))

if __name__ == "__main__":
	main()