'''
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
'''
def solution(s):
    hap = 0
    for _ in range(len(s)):
        hap += _
    if len(s) % 2 != 0:
        return s[hap // len(s)]
    elif len(s) == 2:
        return s
    else:
        return s[hap//len(s) : -(hap//len(s))]

'''
def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1)//2:len(str)//2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))
'''