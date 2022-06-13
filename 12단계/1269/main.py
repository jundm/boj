import sys

A, B = list(map(int, sys.stdin.readline().strip().split()))

M = set(sys.stdin.readline().strip().split())
N = set(sys.stdin.readline().strip().split())
print(len(N - M) + len(M - N))
