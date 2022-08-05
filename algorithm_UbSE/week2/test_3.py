import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
# answer = [-1] * 4 => [-1, -1, -1, -1]
answer = [-1] * n
stack = []

stack.append(0)
print(stack[0])

'''
#for (int i=1;i<n;i++)
# i =1
for i in range(1, n):
    # stack && A[]
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

# 배열 안의 모든 요소들만 출력하는 방식
print(*answer)
'''
