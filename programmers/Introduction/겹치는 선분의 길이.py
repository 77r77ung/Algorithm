from collections import defaultdict
def solution(lines):
    countHash = defaultdict(int)
    dots = []
    array = []
    for _ in lines:
        for i in range(_[0], (_[1]+1)):
            countHash[i] += 1
    print(countHash)
    
    for key, value in countHash.items():
        if value >= 2:
            dots.append(key)
    print(dots)
    
    for _ in range(len(dots)-1):
        if dots[_] +1 == dots[_+1]:
            array.append(dots[_])
            array.append(dots[_+1])
    print(array)
    
    return max(array) - min(array) if len(array) != 0 else 0