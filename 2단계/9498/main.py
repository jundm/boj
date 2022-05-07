import sys

input = int(sys.stdin.readline().strip())

if input>=90:
    print("A")
elif 80<=input<=89:
    print("B")
elif 70<=input<=79:
    print("C")
elif 60<=input<=69:
    print("D")
else:
    print("F")