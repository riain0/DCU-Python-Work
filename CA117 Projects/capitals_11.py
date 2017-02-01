import sys

s = sys.argv[1]

capitalised = s[0].upper() + s[1:-1] + s[len(s)-1].upper()

if len(s) > 1:
	print(capitalised)
