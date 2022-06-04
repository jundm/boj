N = int(input())
const = []
for i in range(1, 1000000):
    x = sum(list(map(int, str(i))))
    if i + x == N:
        const.append(i)
if const:
    print(min(const))
else:
    print(0)
