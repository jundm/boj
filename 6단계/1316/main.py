cnt = int(input())
for i in range((cnt)):
    x = input()
    word = set()
    for i in range(len(x)):
        if x[i] not in word:
            word.add(x[i])
        elif x[i] == x[i - 1]:
            pass
        elif x[i] in word:
            cnt -= 1
            break
print(cnt)
