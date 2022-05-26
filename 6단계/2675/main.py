N = input()

for i in range(int(N)):
    value = input().split()
    for j in value[1]:
        print(j * int(value[0]), end="")
    print()
