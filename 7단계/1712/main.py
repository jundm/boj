A, B, C = list(map(int, input().split()))
# A 고정비용
# B 노트북 한대의 생산비용
# C 노트북 한대의 가격
# C >= A + B
if C > B:
    x = A / (C - B)
    if x > 0:
        print(int(x + 1))
else:
    print(-1)
