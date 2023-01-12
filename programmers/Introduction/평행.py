'''

'''
def solution(dots):
    dots = sorted(dots)
    
    x = [_[0] for _ in dots]
    y = [_[1] for _ in dots]
    
    # print(x)
    # print(y)
    
    if x[1] - x[0] == x[3] - x[2] and y[1] - y[0] == y[3] - y[2]:
        return 1
    elif x[2] - x[0] == x[3] - x[1] and y[2] - y[0] == y[3] - y[1]:
        return 1
    else:
        return 0
    
    if (y[1]-y[0])*(x[1]-x[0])//2 == (y[3]-y[2])*(x[3]-x[2])//2:
        return 1
    elif (y[2]-y[0])*(x[2]-x[0])//2 == (y[3]-y[1])*(x[3]-x[1])//2:
        return 1
    else:
        return 0