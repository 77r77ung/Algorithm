'''
과일 장수가 사과 상자를 포장하고 있습니다.
사과는 상태에 따라 1점부터 k점까지의 점수로 분류하며, k점이 최상품의 사과이고 1점이 최하품의 사과입니다.
사과 한 상자의 가격은 다음과 같이 결정됩니다.
한 상자에 사과를 m개씩 담아 포장합니다.
상자에 담긴 사과 중 가장 낮은 점수가 p (1 ≤ p ≤ k)점인 경우, 사과 한 상자의 가격은 p * m 입니다.
과일 장수가 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익을 계산하고자 합니다.(사과는 상자 단위로만 판매하며, 남는 사과는 버립니다)

사과의 최대 점수 k,
한 상자에 들어가는 사과의 수 m,
사과들의 점수 score가 주어졌을 때,
과일 장수가 얻을 수 있는 최대 이익을 return하는 solution 함수를 완성해주세요.
'''
def solution(k, m, score):
    score = sorted(score, reverse = True)
    result = 0
    for _ in range(len(score)):
        temp = score[m*_ : (_+1)*m]
        if len(temp) == m:
            result += temp[-1] * m * 1
        else:
            result += 0
        #print(temp, result)
    return result