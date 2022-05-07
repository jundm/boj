def solution(S):
    result = []
    for i in range(len(S), 0, -1):
        for j in range(0, len(S)):
            if S[j:i] == "":
                pass
            else:
                result.append(S[j:i])

    return len(set(result))


print(solution(input()))


# s=input()
# l=[]
# for i in range(len(s)):
#    for j in range(i+1,len(s)+1):
#       #print(s[i:j])
#       l.append(s[i:j])
# #print(l)
# print(len(set(l)))
