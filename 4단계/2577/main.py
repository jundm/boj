import sys

input = list(map(int, sys.stdin.read().splitlines()))
value = list((str(input[0] * input[1] * input[2])))
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in value:
    result[int(i)] += 1
for i in result:
    print(i)
