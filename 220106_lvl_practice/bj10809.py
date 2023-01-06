#알파벳 찾기 / Class 1++

import sys

word = sys.stdin.readline()
check = list(range(97, 123))

for i in check:
    print(word.find(chr(i)), end=' ')