a=int(input("첫 번째 숫자 입력: "))
b=int(input("두 번째 숫자 입력: "))

a=int(str(a)[::-1])
b=int(str(b)[::-1])

if(a>b):
    print(a)
else:
    print(b)