'''
1. 수가 주어지면 각 자리의 수를 내림차순으로 정렬해보자.
'''

num = int(input("입력: "))
array = []

for i in str(num):
    array.append(i)

array.sort()
array.reverse()

print("출력: " + array[0] + array[1] + array[2] + array[3])

'''
Python에서는 정수의 길이를 구하기 위해서 문자열로 변환하고 길이를 구해야 한다.
len(str(123))

리스트명.sort(): 오름차순 정렬
리스트명.reverse(): 리스트 항목의 순서를 역순으로 만듦(오름차순-내림차순 개념)
'''

