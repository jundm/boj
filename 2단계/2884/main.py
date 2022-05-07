import sys

input = sys.stdin.readline().strip()
a, b = map(int, input.split())

if b > 44:
    print(a, b - 45)
elif b < 45 and a > 0:
    print(a - 1, b + 60 - 45)
else:
    print(23, b + 60 - 45)
