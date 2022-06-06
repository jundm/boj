N = int(input())

count = 0
x = 0
while True:
    x += 1
    if str(x).find("666") != -1:
        count += 1
        if N == count:
            break
print(x)
