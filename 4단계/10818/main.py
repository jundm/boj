import sys

input = sys.stdin.readline().strip()
input = list(map(int, sys.stdin.readline().strip().split()))

print(min(input), max(input))
