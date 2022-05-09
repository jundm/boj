import sys

input = sys.stdin.readline().strip()
input = sys.stdin.read().splitlines()

for i in range(len(input)):
    x, y = map(int, input[i].split())
    print(x + y)
