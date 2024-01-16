#별 찍기 - 10
import sys

sys.setrecursionlimit(10 ** 6) # 재귀 호출의 깊이 설정 (기본 10**3)

def append_star(LEN):
    if LEN == 1:
        return ['*']

    stars = append_star(LEN // 3)
    L = []

    for S in stars:
        L.append(S * 3)
    for S in stars:
        L.append(S + ' ' * (LEN // 3) + S)
    for S in stars:
        L.append(S * 3)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))