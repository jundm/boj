import sys

N = int(sys.stdin.readline().strip())

count = [0] * 10001
for i in range(N):
    count[int(sys.stdin.readline().strip())] += 1
for i in range(1,10001):
    for j in range(count[i]):
        print(i)
