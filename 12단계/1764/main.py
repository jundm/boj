from sys import stdin

# 듣도보도 못한 사람의 수 N, 보도 못한 사람의 수 M
N, M = list(map(int, stdin.readline().strip().split()))

DontKnow = []
NoSee = []
for i in range(N):
    DontKnow.append(stdin.readline().strip())
for i in range(M):
    NoSee.append(stdin.readline().strip())

s1 = set(DontKnow)
s2 = set(NoSee)
result = list(s1 & s2)
print(len(result), *sorted(result), sep="\n")
