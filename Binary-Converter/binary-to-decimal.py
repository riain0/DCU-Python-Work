import sys


def conv_bin(n):
    decimal = 0
    pw = len(n) - 1
    i = 0
    while i < len(n):
        decimal += int(n[i]) * (2 ** pw)
        pw -= 1
        i += 1
    return decimal


def main():
    bin_str = sys.argv[1]
    print(conv_bin(bin_str))
    

if __name__ == "__main__":
    main()
