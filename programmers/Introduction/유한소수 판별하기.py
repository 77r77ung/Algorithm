'''
소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다.
분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다.
유한소수가 되기 위한 분수의 조건은 다음과 같습니다.
기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.
'''
import math
def solution(a, b):
    gcd = math.gcd(a, b)
    divisor = []
    
    # 소인수분해
    n = 2
    num = b//gcd
    while n <= num:
        if num % n == 0:
            divisor.append(n)
            num = num / n
        else:
            n += 1
    print(divisor)
    
    # 유한소수, 무한소수 판별 -> 차집합으로 접근
    set1 = set(divisor)
    ex = set([2, 5])
    # print(set1)
    # print(ex)
    
    return 1 if len(set1 - ex) == 0 else 2