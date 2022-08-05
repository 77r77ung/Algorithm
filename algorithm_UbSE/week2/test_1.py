'''
[Ubse Algorithm_test] TEST / week2
문제 1. 큐 구현

큐: 선입선출, FIFO(First In First Out)
'''
import sys
N = int(sys.stdin.readline())

queue = []
for i in range(N):
  commend = sys.stdin.readline().split()

  if commend[0] == 'push':
    queue.append(commend[1])
  elif commend[0] == 'pop':
    if len(queue) != 0:
      print(queue[0])
      del(queue[0])
    else:
      print(-1)
  elif commend[0] == 'size':
    print(len(queue))
  elif commend[0] == 'empty':
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  elif commend[0] == 'front':
    if len(queue) != 0:
      print(queue[0])
    else:
      print(-1)
  elif commend[0] == 'back':
    if len(queue) != 0:
      print(queue[-1])
    else:
      print(-1)