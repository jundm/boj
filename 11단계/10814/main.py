import sys

N = int(sys.stdin.readline().strip())
res = [[] for i in range(201)]
for i in range(N):
    x, y = list(map(str, sys.stdin.readline().strip().split()))
    res[int(x)].append((x, y))
re = []
for i in res:
    if i != []:
        re.append(i)
for i in re:
    for j in i:
        print(*j)