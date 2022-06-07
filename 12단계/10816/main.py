# from sys import stdin

# N = int(stdin.readline().strip())
# Ncard = stdin.readline().strip().split()
# M = int(stdin.readline().strip())
# Mcard = stdin.readline().strip().split()
# Mdict = {}
# for i in Mcard:
#     Mdict[i] = 0

# for i in Ncard:
#     if i in Mdict:
#         Mdict[i] = Mdict[i] + 1
# for i in Mcard:
#     print(Mdict[i], end=' ')

#counter 사용

import sys
from collections import Counter
input = sys.stdin.readline

count = Counter()

N=int(input())
cards = list(map(int,input().split()))
for card in cards:
    count[card] += 1

M=int(input())
checks = list(map(int,input().split()))
for check in checks:
    print(count[check], end=' ')