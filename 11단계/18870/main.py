import sys

input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
c = sorted(list(set(l)))
d = {}

rank = 0
for cc in c:
    d[cc] = rank
    rank += 1

for ll in l:
    print(d[ll], end=" ")
