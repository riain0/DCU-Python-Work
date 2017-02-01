import sys

def is_anagram():
	lines = sys.stdin.readlines()
	for line in lines:
		a = line.split()
		for c in a[0]:
			if c not in a[1]:
				ans = False
			else:
				ans = True 
		print(ans)		

def main():
	is_anagram()

if __name__ == "__main__":
	main()