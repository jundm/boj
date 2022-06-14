M = int(input())
N = int(input())


def prime(n):
    if n == 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


primeNumber = []

for i in range(M, N + 1):
    if prime(i) == 1:
        primeNumber.append(i)

if len(primeNumber) != 0:
    print(sum(primeNumber))
    print(min(primeNumber))
else:
    print(-1)
