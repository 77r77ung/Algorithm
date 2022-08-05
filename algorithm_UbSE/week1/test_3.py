'''
[Ubse Algorithm_test] Test / week2
문제 3. 산술평균, 중앙값, 최빈값, 범위 구하기 (중심경향치)

Collections 모듈 - Counter 클래스

TODO) 중앙값
'''

import sys
from collections import Counter

n = int(sys.stdin.readline())

array = list()
for _ in range (n):
    temp = int(sys.stdin.readline())
    array.append(temp)

# 산술평균
hap = 0
for i in array:
    hap += i
    ave = hap / n
# print(ave)

# 중앙값
array.sort()

# 최빈값
counter = Counter(array)
c_n = list(counter.values())
c_k = list(counter.keys())
print(c_n)
for i in counter:
    if c_n.count(max(c_n)):
        c_k.append((map(int, counter.most_common(1), c_k)))
print(c_k)
if c_n.count(max(c_n)) > 1:
    print()
else:
    print(max(counter, key= lambda x: counter[x]))