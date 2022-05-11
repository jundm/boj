import sys

input = list(map(int,sys.stdin.read().splitlines()))
value = max(input)

print(value, input.index(value)+1)
