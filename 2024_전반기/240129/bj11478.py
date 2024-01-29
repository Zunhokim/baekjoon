#서로 다른 부분 문자열의 개수

import sys

S = sys.stdin.readline().rstrip()
ans = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        temp = S[i:j+1]
        ans.add(temp)

print(len(ans))