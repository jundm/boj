import sys

input = int(sys.stdin.readline().strip())


def Fibonacci(n):
    return Fibonacci(n - 1) + Fibonacci(n - 2) if n >= 2 else n


print(Fibonacci(input))
