'''
두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.
a + b = c
'''
a, b = map(int, input().strip().split(' '))
print("{a} + {b} = {c}".format(a=a, b=b, c=a+b))
'''
a, b = map(int, input().strip().split(' '))
print(f"{a} + {b} = {a + b}")
'''