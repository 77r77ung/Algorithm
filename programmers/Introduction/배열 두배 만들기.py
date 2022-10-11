'''
정수 배열 numbers가 매개변수로 주어집니다.
numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

* lambda를 사용해서도 풀어보기
'''
def solution(numbers):
    return [_*2 for _ in numbers]

# lambda 사용해서 풀어보기
def solution(numbers):
    return list(map(lambda x : x*2, numbers))
    
print(solution([1, 2, 3, 4, 5]))