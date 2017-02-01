import sys

def word_count(s):
	s = s.split()
	return len(s)


lines = sys.stdin.read()
print(word_count(lines))