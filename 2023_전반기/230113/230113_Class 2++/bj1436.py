#영화감독 숌

import sys

N = int(sys.stdin.readline())

key = 666
count = 0

while True:
    if '666' in str(key):
        count += 1
    if count == N:
        print(key)
        break
    key += 1
