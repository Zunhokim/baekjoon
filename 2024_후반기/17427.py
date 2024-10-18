import sys

N = int(sys.stdin.readline())
answer = 0
for number in range(1, N+1):
    answer += (number) * (N//number)

print(answer)