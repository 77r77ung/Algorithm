'''
[Ubse Algorithm_test] Homework / week5
문제 1. 문자열(가장 많이 사용된 알파벳 출력)

Collections 모듈 - Counter 클래스
'''

import collections

word = input().upper()
counter = collections.Counter()
counter.update(word)
print(counter)

# counter 딕셔너리의 value 값을 list로 저장
c_n = list(counter.values())

# 가장 많이 사용된 알파벳(max(c_n))이 1개 이상일 경우(c_n.count를 이용해 max(c_n)의 개수를 셈)
if c_n.count(max(c_n)) > 1:
    print('?')
# 가장 많이 사용된 알파벳 출력
else:
    print(max(counter, key=lambda x: counter[x]))