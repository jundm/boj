word = input()

double = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
triple = ["dz="]

n, answer = len(word), len(word)
word += "~~"

for i in range(n):
    print(word[i : i + 3])
    if word[i : i + 2] in double:
        answer -= 1
    if word[i : i + 3] in triple:
        answer -= 1

print(answer)
