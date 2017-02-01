import sys
from operator import itemgetter

p_scores = {}

def get_handicap(i, hc):
    return hc // 18 + (i <= hc % 18)

def get_scores(inp, p, i):
    for j, v in enumerate(inp):
        player = " ".join(inp[j][:-19])
        strokes = inp[j][-18:]
        t = 0
        for k, s in enumerate(strokes):
            score = 0
            if s != "X":
                hc = get_handicap(i[k], int(inp[j][-19]))
                score += int(s) - p[k] - hc
                if score < 2:
                    t += (score * -1) + 2
        p_scores[player] = t
    return p_scores

def main():
    l = [s.strip().split() for s in sys.stdin]
    par = [int(n) for i, n in enumerate(l[0])]
    index = [int(v) for i, v in enumerate(l[1])]
    d = get_scores(l[2:], par, index)
    longest_name = max([name for name in d], key=len)
    for name, score in sorted(d.items(), reverse=True, key=itemgetter(1)):
        print("{1:>{0}} : {2:>2}".format(longest_name, name, score))


if __name__ == "__main__":
	main()
