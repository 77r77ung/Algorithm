'''
[Ubse Algorithm_test] Homework / week2
문제 1. 스택 구현
'''

import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            # stack에서 원소를 빼지 않고 제일 마지막 항목을 가져오고만 싶을 때 stack명[-1]
            print(stack[-1])