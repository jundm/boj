import sys

N = int(sys.stdin.readline().strip())
res = []
for i in range(N):
    x,y = list(map(int,sys.stdin.readline().strip().split()))
    res.append((x,y))
for i in sorted(res):
    print(*i)

