# import sys

# C = int(input())
# input = sys.stdin.read().splitlines()

# for j in range(C):
#     result = 0
#     exam = list(map(int, input[j].split()))[1:]
#     N = len(exam)
#     # N = int(input[j][0])
#     for i in exam:
#         result += i
#     Average = result / N

#     aboveAvg = 0
#     for i in exam:
#         if i > Average:
#             aboveAvg += 1
#     print("%.3f" % ((aboveAvg / N) * 100) + "%")

#딱군이 풀이
from functools import reduce
import sys

c = int(input())

for _ in range(c):
   data = list(map(int, sys.stdin.readline().split()))
   n, scores = data[0], data[1:]
   average = sum(scores) / n
   students_above_avg = reduce(lambda acc, x : acc + (1 if x > average else 0), scores, 0)
   print(f'{round(students_above_avg / n * 100, 3):.3f}%')
