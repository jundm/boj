# def factorial(i):
#     if i == 1:
#         return 1
#     if i > 0:
#         return i * factorial(i - 1)

# print(factorial(int(input())))
# 이거 아님

def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n - 1)
    return result

n = int(input())
print(factorial(n))