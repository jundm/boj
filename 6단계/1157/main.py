input = input().lower()
alphabet = [0 for i in range(26)]

for i in input:
    alphabet[ord(i) - 97] += 1
tmp = max(alphabet)
index = alphabet.index(tmp)
questionMark = 0

for i in alphabet:
    if i == tmp:
        questionMark += 1

if questionMark == 1:
    print(chr(index + ord("A")))
else:
    print("?")
