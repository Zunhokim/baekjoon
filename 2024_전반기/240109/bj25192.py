#인사성 밝은 곰곰이
import sys

N = int(sys.stdin.readline())
chat_log = set()
gom = set()
cout = 0


for i in range(N):
    user = sys.stdin.readline().strip()
    if user == 'ENTER':
        cout += len(gom)
        gom = set()
    else:
        gom.add(user)

cout += len(gom)
print(cout)