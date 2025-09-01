a, b = input().split()
L = len(a)
print(min(sum(x != y for x, y in zip(a, b[i:i+L])) for i in range(len(b) - L + 1)))
