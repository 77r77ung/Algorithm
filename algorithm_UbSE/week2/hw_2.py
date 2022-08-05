'''
[Ubse Algorithm_test] Homework / week2
문제 2. 스택 (백준 스택: 10773번 문제)
'''

import sys
k = int(sys.stdin.readline())

stack = []
for _ in range(k):
    temp = int(sys.stdin.readline())
    
    if temp == 0:
        stack.pop()
    else:
        stack.append(temp)

hap = 0
for i in stack:
    hap += i

print(hap)