'''
[Ubse Algorithm_test] Homework / week5
문제 3. 문자열(입력으로 주어진 N 숫자의 합계)
'''

print(sum(map(int, input())))

'''
reduce: 시퀀스(문자열, 리스트, 튜플)의 원소들을 누적해 lambda 함수 적용
from functools import reduce
N = list(map(int, input()))
print(reduce(lambda x, y: x + y, N))
'''