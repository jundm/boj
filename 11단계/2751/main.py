import sys

N = int(sys.stdin.readline().strip())
res = []
for i in range(N):
    res.append(int(sys.stdin.readline()))
for i in sorted(res):
    print(i)
