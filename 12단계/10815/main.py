import sys

# 카드의 집합을 만들어 특정 카드가 집합에 있는지 빠르게 찾는 문제

N = int(sys.stdin.readline().strip())
Ncard = set(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
Mcard = list(map(int, sys.stdin.readline().strip().split()))
res = []
for i in Mcard:
    if i in Ncard:
        res.append(1)
    else:
        res.append(0)
print(*res)
