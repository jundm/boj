import sys

testCaseLength = sys.stdin.readline()
input = sys.stdin.read().splitlines()

for i in range(len(input)):
    x, y = map(int, input[i].split())
    print(x + y)
