'''
[Ubse Algorithm_test] Homework / week2
문제 4. 카드 2
큐: 선입선출, FIFO(First In First Out)

TODO collections 사용해서 구현
'''
import sys
N = int(sys.stdin.readline())

queue = list(range(1, N+1))

# queue의 요소가 하나만 남을 때까지
while (len(queue) > 1):
    queue.pop(0)
    temp = queue.pop(0)
    queue.append(temp)

print(queue)
print(queue.pop(0))

