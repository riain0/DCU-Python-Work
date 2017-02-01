import sys

def main():
	s = sys.argv[1]
	if len(s) % 2 == 0:
		print("No middle character!")
	else:
		print(s[int(len(s) / 2)])

if __name__ == "__main__":
	main()