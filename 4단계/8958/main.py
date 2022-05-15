import sys

input = sys.stdin.read().splitlines()[1:]

for j in range(len(input)):
    X = 0
    result = 0
    for i in input[j]:
        if i == "O":
            X += 1
        else:
            X = 0
        result += X
    print(result)
