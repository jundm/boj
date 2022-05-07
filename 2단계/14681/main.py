import sys

input = sys.stdin.readlines()
input = list(map(lambda s: int(s.strip()), input))

if input[0]>0 and input[1]>0:
    print(1)
elif input[0]<0 and input[1]>0:
    print(2)
elif input[0]<0 and input[1]<0:
    print(3)
elif input[0]>0 and input[1]<0:
    print(4)
