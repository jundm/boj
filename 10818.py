def solution(numbers):

    return min(numbers), max(numbers)


N = int(input())
numbers = list(map(int, input().split()))
print(solution(numbers))


# # f = open("input.txt", 'r')
# # input = f.readline


# def solution(value):

#     numbers = list(map(int, value.split()))

#     return min(numbers), max(numbers)


# N = int(input())
# s = solution(input())

# print(s[0], s[1])


# def solution(value):

#     numbers = list(map(int, value.split()))

#     return min(numbers), max(numbers)


# N = int(input())

# print(*solution(input()))


# def solution(value):

#     numbers = list(map(int, value.split()))

#     return str(min(numbers)) + " " + str(max(numbers))


# N = int(input())

# print(solution(input()))
# a = 4
# b = 3
# c = a//b
# d = a/b
# print(c, d)

