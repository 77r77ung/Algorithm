'''
점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(dots):
    case = []
    # case1: dot1 - dot2
    case.append((dots[0][1]-dots[1][1]) / (dots[0][0]-dots[1][0]))
    # case2: dot1 - dot3
    case.append((dots[0][1]-dots[2][1]) / (dots[0][0]-dots[2][0]))
    # case3: dot1 - dot4
    case.append((dots[0][1]-dots[3][1]) / (dots[0][0]-dots[3][0]))
    # case4: dot2 - dot3
    case.append((dots[1][1]-dots[2][1]) / (dots[1][0]-dots[2][0]))
    # case5: dot2 - dot4
    case.append((dots[1][1]-dots[3][1]) / (dots[1][0]-dots[3][0]))
    # case6: dot3 - dot4
    case.append((dots[2][1]-dots[3][1]) / (dots[2][0]-dots[3][0]))
    
    print(case)
    print(set(case))
    return 1 if len(set(case)) != len(case) else 0