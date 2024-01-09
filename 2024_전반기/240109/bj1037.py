#약수
#N의 진짜 약수를 줬을 때, N을 파악 하는 문제

case = int(input())
real = list(map(int, input().split()))
real.sort()

num = real[0] * real[-1]
print(num)