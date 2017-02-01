import sys

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

encrypted = sys.stdin.read()
a = [c for c in encrypted if c.isalnum()]
counter = {}
for c in a:
    counter[c] = encrypted.count(c)
count = max(counter, key=counter.get)
diff = 4 - alpha.index(count)
shift = alpha[diff:] + alpha[:diff]
decrypt = {}
for i in range(0, len(alpha)):
    decrypt[alpha[i]] = shift[i]
decrypted = [decrypt[c] if c in decrypt else c for c in encrypted]
print("".join(decrypted))
