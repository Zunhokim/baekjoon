#나는야 포켓몬 마스터
import sys

N, M = map(int, sys.stdin.readline().split())
num = {}
name = {}

for i in range(1, N+1):
    case = sys.stdin.readline().rstrip()
    num[i] = case
    name[case] = i

for _ in range(M):
    case = sys.stdin.readline().rstrip()
    if case.isdigit():
        print(num[int(case)])
    else:
        print(name[case])