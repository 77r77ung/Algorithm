num=int(input("개수: "))
array = []

for i in range(num):
    array.append(int(input("숫자 입력: ")))
    
array.sort()

for j in array:
    print(j)