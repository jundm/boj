import sys

input = int(sys.stdin.readline().strip())

if (input % 4 == 0 and input % 100 != 0) or (input % 400 == 0):
    print(1)
else:
    print(0)
