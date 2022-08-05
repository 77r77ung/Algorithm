'''
[Ubse Algorithm_test] Homework / week5
문제 4. 문자열(다이얼)
'''
dial = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

word = list(map(str, input()))
print(word)

sec = 0

# enumerate로 배열을 인덱스와 바로 연결(j: index k: 원소)
for i in word:
    for j, k in enumerate(dial):
        if i in k:
            sec += j + 3
            print(sec)

'''
# 인덱스의 시작을 3으로 지정
for i in word:
    for j, k in enumerate(dial, start=3):
        if i in k:
            sec += j
            print(sec)
'''