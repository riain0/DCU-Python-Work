import sys

a = sys.stdin.read().split("\n")

def letters_17():
	return [w for w in a if len(w) == 17]


def letters_over_17():
	return[w for w in a if len(w) > 17]


def shortest_vowel():
	return [w for w in a if all(c in w for c in ["a", "e", "i", "o", "u"])]


def four_a():
	return [w for w in a if w.count("a") == 4]


def two_q():
	return [w for w in a if w.count("q") >= 2]


def contains_cie():
	return [w for w in a if "cie" in w]


def angle():
	return [w for w in a if all(c in w for c in ["a", "n", "g", "l", "e"]) and len(w) == 5 and w != "angle"]


def iary():
	return [w for w in a if w.endswith("iary")]


def qu():
	return [w for w in a if "q" in w and "qu" not in w]


def most_e():
	return [w for w in a if w.count("e") > 4]


def main():
	print("Words containing 17 letters:", letters_17())
	print("Words containing 18+ letters:", letters_over_17())
	print("Shortest word containing all vowels:", min(shortest_vowel(), key=len))
	print("Words with 4 a's:", four_a())
	print("Words with 2+ q's:", two_q())
	print("Words containing cie:", contains_cie())
	print("Anagrams of angle:", angle())
	print("Words ending in iary:", len(iary()))
	print("Words with q but no u:", qu())
	print("Words with most e's:", most_e())


if __name__ == "__main__":
	main()