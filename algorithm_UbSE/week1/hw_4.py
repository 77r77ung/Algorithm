'''
4. 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램
    a) 길이가 짧은 것부터
    b) 길이가 같으면 사전 순으로
    TODO 조건)문자열의 길이는 50을 넘지 않는다.
    for j in arr:
        if int(len(arr[j])) > 50:
            del(arr[i])
    TODO 조건)대문자가 입력되었을 때
    TODO 조건)단어의 개수에 대한 조건 (1 <= N <= 20000)

    arr.sort(): 알파벳 순서로 정렬
'''
arr = []

num = int(input("단어의 개수: "))
for i in range(num):
    arr.append(input("소문자로 구성된 단어를 입력하세요.: "))

new = list(set(arr))
new.sort(key = lambda x : (len(x), x))
print(new)

'''
import sys

# sys.stdin.readline(): input보다 입력 시간을 줄여줌
count = int(sys.stdin.readline())

words = list()

for _ in range(count):
    words.append(input())

# set(배열명): 중복 제거, 순서가 없어짐
# list(set(배열명)): 중복을 제거해주고 그 요소들을 list로 다시 만들어줌
words = list(set(words))

# 사전 순으로 정렬 (sort의 default: 사전순)
words.sort()

# 길이 순으로 다시 정렬
words.sort(key = len)

for word in words:
    print(word)

!! 배열명.sort(key = lambda x : (len(x), x))
lamda를 쓰는 것과 그냥 key = len으로 사용하는 것의 차이점은 무엇일까?
'''