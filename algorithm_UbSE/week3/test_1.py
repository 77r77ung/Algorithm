import sys

s = []
s_top = 0
n = int(sys.stdin.readline())

# 리스트를 스택으로 구현
top = n
a = list(map(int, sys.stdin.readline().split()))

for i in range(n-1):
    top -= 1
    outNum = a.pop()

    if a[i] < outNum:
        s_top += 1
        s.append(outNum)
    elif a[i] >= outNum:
        top -= 1
    else:
        print(-1)

print()