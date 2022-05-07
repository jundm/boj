import sys

input = sys.stdin.readline().strip()
A,B,C = map(int,input.split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)


