import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))

Nword = set([sys.stdin.readline().strip() for i in range(N)])
Mword = [sys.stdin.readline().strip() for i in range(M)]
count = 0
for i in Mword:
    if i in Nword:
        count += 1
print(count)
