# import sys

# input = sys.stdin.readline().strip()
# x, y, z = map(int, input.split())

# if x == y == z:
#     print(10000 + (x * 1000))
# elif x == y or x == z:
#     print(1000 + (x * 100))
# elif y == z:
#     print(1000 + (y * 100))

# else:
#     print(max(x, y, z) * 100)

*_,a,b,c=sorted(input())

print(['1'+b,c][a<b<c]+'000'[a<c:])