#검증수 / Class 1++
import sys

num = sys.stdin.readline().split()
check = 0

for i in num:
    check += int(i)**2

print(check % 10)