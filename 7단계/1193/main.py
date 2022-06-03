# 짝수 분자 커짐 분모 작아짐
# 홀수 분자 작아짐 분모 커짐
# 숫자 리스트안에 요소의 개수
# 이어서 봤을때 예제 입력의 숫자는 인덱스라고 볼수 있을듯
# 표로 보면 x축은 분자가 고정 세로로는 1씩 증가하는 표
# y축은 분모가 고정 x축으로는 1씩증가
# 인덱스+표의 관계만 찾아내면 될듯
# 세로 인덱스 규칙 1,3,4,10,11 1,2,6,7,
# 가로 인덱스 규칙 1,2,6,7,15  1,4,8

# # 표만들기
# for x in range(1, 11):
#     for y in range(1, 11):
#         print(f"{x}/{y}", end=" ")
#     print(" ")

# n(n+1)/2
# input = 3
# m=(input - 1)*((input - 1)+1)//2
# n=(input + 1)*((input + 1)+1)//2
# print(m,n)


# array = []
# for i in range(1, 10000001):
#     for j in range(1,i):
#         if i % 2 == 1:
#             array.append(f'{j}/{i-j}')
#         elif i % 2 == 0:
#             array.append(f'{i-j}/{j}')

# print(array[input-1])

# num = 100
# start = 0 # 더해지는 수
# end = 0 # 몇까지 더해야 num에 닿을까
# while end < num :
#     start += 1
#     end += start
# print(start) # 100은 start번째 괄호 안에 있음
# used = end - start
# position = num - used # 100은 start번째 괄호 안에서 position번째 수임
# print(position)


num = input()
start = 0  # 더해지는 수
end = 0  # 몇까지 더해야 num에 닿을까
while end < num:
    start += 1
    end += start
print(start)  # 100은 start번째 괄호 안에 있음

if start % 2 == 0:
    bunmo = list(range(1, start + 1))[::-1]
    bunja = list(range(1, start + 1))
elif start % 2 == 1:
    bunmo = list(range(1, start + 1))
    bunja = list(range(1, start + 1))[::-1]

used = end - start
position = num - used  # 100은 start번째 괄호 안에서 position번째 수임
print( str(bunja[position-1]) + '/' + str(bunmo[position-1]) )