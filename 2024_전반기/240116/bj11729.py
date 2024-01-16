#하노이 탑 이동 순서

import sys
def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, start, 6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)

N = int(sys.stdin.readline().rstrip())
print(2**N-1)
hanoi(N, 1, 3)