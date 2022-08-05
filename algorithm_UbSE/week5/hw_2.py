'''
[Ubse Algorithm_test] Homework / week5
문제 2. 문자열(문자열 반복)
'''

import sys

# Testcase 입력 받음
t = int(sys.stdin.readline())

for _ in range(t):
    r, s = list(map(str, sys.stdin.readline().split()))
    # 문자열 s(list)를 r만큼 반복한 뒤 정렬해 새로운 list s1을 생성 / ''.join을 이용해 하나의 문자열로 합침
    s1 = ''.join(sorted(s * int(r)))
    print(s1)

'''
for _ in range(t):
    r, s = list(map(str, sys.stdin.readline().split()))
    s1 = sorted(s * int(r))

    for s1 in s1:
        print(s1, end="")
'''
