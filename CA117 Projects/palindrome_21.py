import sys

def is_palindrome(s):
	is_palindrome = True
	a = list(s.lower())
	for i, c in enumerate(a):
		if not c.isalnum():
			a[i] = ""

	s = "".join(a)
	if s != s[::-1]:
		is_palindrome = False
	return is_palindrome

def main():
	print(is_palindrome(sys.argv[1]))

if __name__ == "__main__":
	main()