#숫자의 합
import sys

N = int(sys.stdin.readline())
num = sys.stdin.readline()
count = 0

for i in range (N):
    count += int(num[i])


print(count)