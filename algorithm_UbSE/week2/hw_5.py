'''
[Ubse Algorithm_test] Homework / week2
문제 5. 덱 구현
덱: 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조의 한 형태

TODO front 출력 안 됨 해결!
'''
import sys
N = int(sys.stdin.readline())

deque = []
for i in range(N):
    commend = sys.stdin.readline().split()

    if commend[0] == 'push_front':
        deque.insert(0, commend[1])
    elif commend[0] == 'push_back':
        deque.append(commend[1])
    elif commend[0] == 'pop_front':
        if len(deque) != 0:
            print(deque[0])
            del(deque[0])
        else:
            print(-1)
    elif commend[0] == 'pop_back':
        if len(deque) != 0:
            deque.pop()
            print(deque.pop())
        else:
            print(-1)
    elif commend[0] == 'size':
        print(len(deque))
    elif commend[0] == 'empty':
        if len(deque) == 0:
            print(0)
        else:
            print(1)
    elif commend[0] == 'fornt':
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif commend[0] == 'back':
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)