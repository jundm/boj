import sys
input = list(map(int, sys.stdin.read().splitlines()))
result = []
for i in input:
    result.append(i % 42)
print(len(set(result)))