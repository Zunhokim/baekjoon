import sys

n = int(sys.stdin.readline())
stack = []
ans = []
count = 1
temp = True

for i in range(n):
    num = int(sys.stdin.readline())

    while count <= num:
        stack.append(count)
        ans.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')

    else:
        temp = False

if temp == False:
    print('NO')

else:
    for i in ans:
        print(i)