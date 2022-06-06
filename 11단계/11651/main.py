import sys

N = int(sys.stdin.readline().strip())
res = []
for i in range(N):
    x, y = list(map(int, sys.stdin.readline().strip().split()))
    res.append((y, x))
res.sort()
for y,x in res:
    print(x,y)