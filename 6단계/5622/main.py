dial = list(input())
time = 0
for i in dial:
    if ord("A") <= ord(i) <= ord("C"):
        time += 3
    elif ord("D") <= ord(i) <= ord("F"):
        time += 4
    elif ord("G") <= ord(i) <= ord("I"):
        time += 5
    elif ord("J") <= ord(i) <= ord("L"):
        time += 6
    elif ord("M") <= ord(i) <= ord("O"):
        time += 7
    elif ord("P") <= ord(i) <= ord("S"):
        time += 8
    elif ord("T") <= ord(i) <= ord("V"):
        time += 9
    elif ord("W") <= ord(i) <= ord("Z"):
        time += 10
print(time)
