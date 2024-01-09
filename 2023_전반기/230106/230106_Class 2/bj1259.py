#펠린드롬수

import sys

word_list = []
word = 1

while True:
    word = sys.stdin.readline().strip()
    if word != '0':
        word_list.append(word)
    else:
        break

for i in word_list:
    if i == i[::-1]:
        print('yes')
    else:
        print('no')