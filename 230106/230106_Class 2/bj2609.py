#최대공약수와 최소공배수
import sys
import math

A = sys.stdin.readline().split()

print(math.gcd(int(A[0]), int(A[1])))
print(math.lcm(int(A[0]), int(A[1])))