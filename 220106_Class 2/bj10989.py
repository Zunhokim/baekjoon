#수 정렬하기 3

import sys

N = int(sys.stdin.readline())

check = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    check[num] = check[num] + 1

for i in range(10001):
    if check[i] != 0:
        for j in range(check[i]):
            print(i)


#이 문제의 경우에는, 메모리 제한이 있기 때문에, list.append를 활용해서 문제 풀이를 했을 경우에는 메모리 초과 현상이 발생했다.
#따라서, 문제 조건인, 10000이라는 숫자를 바탕으로 하여, 10001개(0~9999까지니까 10000으로 하면)의 인덱스를 생성하여 해당하는 숫자가 있을 경우 인덱스의 숫자를 1 증가 시켰다.