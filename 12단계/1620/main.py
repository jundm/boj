import sys
input = sys.stdin.readline

N, M = map(int, input().split())
book = {}

for n in range(N):
    pokemon = input().strip()
    book[pokemon] = str(n+1)
    book[str(n+1)] = pokemon
for m in range(M):
    pokemon = input().strip()
    print(book[pokemon])
