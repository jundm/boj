import sys
N = int(sys.stdin.readline().strip())
input = list(map(int, sys.stdin.readline().strip().split()))
max = max(input)
print((sum(input) * 100) / (N * max))
