import sys

input = sys.stdin.readline().strip()
input = sys.stdin.read().splitlines()
for i in range(len(input)):
    A, B = map(int, input[i].split())
    print(f"Case #{i+1}: {A+B}")
