n, x = map(int, input().split())

num = list(map(int, input().split()))
array = list()

for i in range(n):
    if num[i] < x:
        array.append(num[i])

array = list(set(array))
# array.sort()

for array in array:
    print(array)