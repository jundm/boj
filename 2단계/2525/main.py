# import sys

# input = sys.stdin.readlines()
# input = list(map(lambda s: s.strip(), input))

# h, m = map(int, input[0].split())
# cookingTime = int(input[1])

# if m + cookingTime <= 60 and h < 23:
#     print(f"{h} {m+cookingTime}")
# elif m + cookingTime >= 60 and h < 23:
#     print(f"{h+((m+cookingTime)//60)} {(m+cookingTime) % 60}")
# elif m + cookingTime < 60 and h == 23:
#     print(f"{h} {(m+cookingTime) % 60}")
# elif m + cookingTime >= 60 and h == 23:
#     print(
#         f"{((m+cookingTime)//60)-1 if ((m+cookingTime)//60)-1<24 else(((m+cookingTime)//60)-1)%24} {(m+cookingTime) % 60}"
#     )


h, m = map(int, input().split())
time = int(input())

m += time
h, m = h + m//60, m%60
print(h%24, m)

a,b=map(int,input().split())
d=int(input())
t=(a*60)+b+d
b=t%60
t=t//60
a=t%24
print(a,b)