import sys

input = int(sys.stdin.readline().strip())
i = 2
while input != 1:
    if input % i == 0:
        input = input / i
        print(i)
    else:
        i += 1
