n = int(input())
board = [["*"] * n for i in range(n)]


def star(k):
    if k == n:
        return
    for i in range(k):
        for j in range(k):
            c = board[i][j]
            board[i][j + k] = c
            board[i][j + 2 * k] = c
            board[i + k][j] = c
            board[i + k][j + k] = " "
            board[i + k][j + 2 * k] = c
            board[i + 2 * k][j] = c
            board[i + 2 * k][j + k] = c
            board[i + 2 * k][j + 2 * k] = c
    star(3 * k)


star(1)
for i in range(n):
    for j in range(n):
        print(board[i][j], end="")
    print()
