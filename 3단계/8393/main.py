import sys

input = int(sys.stdin.readline().strip())

sum = 0
for i in range(input + 1):
    sum = sum + i
print(sum)
