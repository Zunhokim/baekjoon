#영단어 암기는 괴로워

import sys

N, M = map(int, sys.stdin.readline().split(" "))
dictionary = dict()

for i in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1

result = sorted(dictionary, key = lambda x: (-dictionary[x], -len(x), x))

for i in result:
    print(i)