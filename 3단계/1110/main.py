# 안풀려서 도움 받았습니다. 제 코드가 아닙니다.
def next(n: str):
    second = str(int(n[0]) + int(n[1]))[-1]
    first = n[-1]
    return first + second


def next_int(n: int):
    first = n % 10
    second = ((n // 10) + (n % 10)) % 10
    return first * 10 + second


s = input()
if len(s) == 1:
    s = "0" + s
t = s
count = 1

while True:
    if next(t) == s:
        break
    else:
        count += 1
        t = next(t)

print(count)
