'''
[Ubse Algorithm_test] Homework / week2
문제 3. 스택 수열

* 스택: LIFO, Last in First out (후입선출 알고리즘)
'''
import sys
n = int(sys.stdin.readline())

stack = []
result = []
count = 0
for i in range(n):
    temp = int(sys.stdin.readline())

    while count < temp:
        count += 1
        stack.append(count)
        result.append('+')
    
    if stack[-1] == temp:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit(0)

for _ in result:
    print(_)