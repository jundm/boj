import sys

input = int(sys.stdin.readline().strip())

value = list(map(int, sys.stdin.readline().strip().split()))
count = 0


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


for i in value:
    if prime(i) == 1 and i != 1:
        count += 1
print(count)
# def is_prime(n):
#   for i는 2부터 math.sqrt(n)까지:
#     if n을 i로 나눠봤는데 나눠지면:
#       return 소수 아님 false
#   # 다 돌아봤지만 나눠지는 경우가 없어서 여기까지 옴
#   return 소수 맞음 true