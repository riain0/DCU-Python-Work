import sys

def main():
	s = sys.argv[1]
	sub_s = sys.argv[2]

	if sub_s in s:
		print(True)
	else: 
		print(False)

if __name__ == "__main__":
	main()