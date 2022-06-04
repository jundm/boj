N = int(input())

guys = []
rank = []

for n in range(N):
    x, y = map(int, input().split())
    guys.append((x, y))

for (x, y) in guys:
    # print(x, y)
    count = 0
    for (p, q) in guys:
        if p > x and q > y:
            count += 1
            # print(count)
    rank.append(count + 1)

print(*rank)
