import sys

def get_occurences(matrix, seq):
    total = [0, 0, 0, 0, 0]
    for i, line in enumerate(matrix):
        for j, c in enumerate(line):
            if c == "x":
                total[0] += 1
                if total[0] == seq:
                    total[4] += 1
                for k in range(0, seq):
                    try:
                        if matrix[i + k][j] == matrix[k + i + 1][j] == "x":
                            total[1] += 1
                            if total[1] == seq - 1:
                                total[4] += 1
                        else:
                            total[1] = 0
                    except Exception:
                        pass

                    try:
                        if matrix[i + k][k + j] == matrix[k + i + 1][k + j + 1] == "x":
                            total[2] += 1
                            if total[2] == seq - 1:
                                total[4] += 1
                        else:
                            total[2] = 0
                    except Exception:
                        pass
                    try:
                        if matrix[i + k][j - k] == matrix[k + i + 1][j - k - 1] == "x":
                            total[3] += 1
                            if total[3] == seq - 1:
                                total[4] += 1
                        else:
                            total[3] = 0
                    except Exception:
                        pass
            else:
                total[0] = 0
    if seq == 1:
        return total[4] * 4
    else:
        return total[4]

def main():
    seq = int(sys.argv[1])
    matrix = [line.strip() for line in sys.stdin]
    print(get_occurences(matrix, seq))

if __name__ == '__main__':
    main()
