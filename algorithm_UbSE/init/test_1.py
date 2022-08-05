num = int(input("숫자를 입력하세요.: "))

for i in range(num+1):
    print(' '*(num-i)+'*'*i)