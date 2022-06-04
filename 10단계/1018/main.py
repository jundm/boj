n, m = map(int, input().split())

chess = []

for _ in range(n):
    chess.append(list(map(str, input())))


def scan(x, y):
    b_start = 0
    w_start = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if chess[x + i][y + j] == "W":
                    b_start += 1
                else:
                    w_start += 1
            else:
                if chess[x + i][y + j] == "B":
                    b_start += 1
                else:
                    w_start += 1
    return min(b_start, w_start)



answer = 64

for x in range(n - 7):
    for y in range(m - 7):
        answer = min(answer, scan(x, y))

print(answer)
