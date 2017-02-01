import string
import sys

def unique_words(s):
	s = s.split()
	seen = []
	for w in s:
		w = w.lower()
		if w[-1] in string.punctuation:
			w = w[:-1]
		if w not in seen and w.isalnum():
			seen.append(w)
	return len(seen)

def main():
	line = sys.stdin.read()
	print(unique_words(line))

if __name__ == "__main__":
	main()
