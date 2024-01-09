import sys

n = int(sys.stdin.readline())
str_ = list(input())
res = 0

for i in range(n):
    res += ((ord(str_[i]) - 96) * (31 ** i))

print(res % 1234567891)
