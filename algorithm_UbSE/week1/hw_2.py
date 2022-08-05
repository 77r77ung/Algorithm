'''
2. N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램 작성
    -> while문과 리스트(list)를 이용해 엔터(Enter)가 두 번 입력되면 입력을 종료하는 프로그램 작성
'''
array = []

while True:
    i = input("입력: ")
    array.append(i)
    if not i:
        break

array.pop()
new = list(set(array))
new.sort()

for j in new:
    print(j)