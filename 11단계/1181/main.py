import sys
import itertools

"""
문자열길이 50개까지니까 for문으로 res*i=[] 를 50개까지 만듦 ㅇ
글자수 1개면 res1에다가 어펜드 ㅇ
그리고 생성된애들 글자수 똑같은애들끼리 sorted ㅇ
나머지애들 전부 concat ㅇ
중복제거 ㅇ
"""
N = int(sys.stdin.readline().strip())
# 단어의 길이 순으로 정렬하기
res = [[] for i in range(51)]
for i in range(N):
    word = sys.stdin.readline().strip()
    res[len(word)].append(word)
re = []
for i in res:
    if i != []:
        re.append(sorted(list(set(i))))
for i in list(itertools.chain(*re)):
    print(i)
