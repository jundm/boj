# import sys

# N, X = map(int, sys.stdin.readline().strip().split())
# input = list(map(int, sys.stdin.readline().strip().split()))
# output = []
# for i in range(len(input)):
#     if input[i] < X:
#         output.append(str(input[i]))
# result = ' '.join(s for s in output)
# print(result)



a,b = map(int, input().split())
lst = list(map(int,input().split()))

for i in range(a):
    if lst[i]< b:
        print(lst[i],end=" ")
