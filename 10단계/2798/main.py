N, M = list(map(int, input().split()))
card = list(map(int, input().split()))

result = 0
for i in card:
    for j in card:
        for k in card:
            if i == j:
                pass
            elif j == k:
                pass
            elif i == k:
                pass
            else:
                sum = i + j + k
                if sum > M:
                    pass
                elif sum <= M:
                    result = max(sum, result)
print(result)
