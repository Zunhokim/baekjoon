#덩치

import sys

N = int(sys.stdin.readline())
student = []

for i in range (N):
    man = list(map(int, sys.stdin.readline().split()))
    student.append(man)

for i in student:
    rank = 1
    for j in student:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end= ' ')