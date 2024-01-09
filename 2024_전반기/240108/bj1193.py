#분수찾기

num = int(input())
line = 1

while num > line:
    num -= line
    line += 1

if line % 2 == 0:
    A = num
    B = line - num + 1
elif line % 2 == 1:
    A = line - num + 1
    B = num

print(f"{A}/{B}")