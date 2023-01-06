#단어 정렬
import sys

word_list = []
N = int(sys.stdin.readline())

for i in range (N):
    word = sys.stdin.readline().strip()
    word_list.append(word)

cash_list = set(word_list)
word_list = list(cash_list)

word_list.sort()
word_list.sort(key = len)

for i in word_list:
    print(i)