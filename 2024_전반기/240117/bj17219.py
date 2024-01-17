#비밀번호 찾기

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
site = []
password = []
search = []

for i in range(N):
    case_s, case_p = sys.stdin.readline().rstrip().split()
    site.append(case_s)
    password.append(case_p)

for i in range(M):
    case = sys.stdin.readline().rstrip()
    search.append(case)

for i in search:
    print(password[site.index(i)])