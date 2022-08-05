'''
3. 회원 정보가 현재 가입 순으로 가입되어 있어 이를 정렬하고자 함.
    나이 순으로 정렬한 후 나이가 같다면 먼저 가입한 회원이 앞으로 오는 순서로 정렬하는 프로그램을 작성하세요.
    -> Stack
'''

arr = []
top = 0

num = int(input("온라인 저지 회원의 수: "))

for i in range(num):
    arr.append(input("입력: "))
    top += 1

arr.sort()
print(arr)

'''
TODO 조건)온라인 저지 회원의 수 조건(1 <= N <= 100000)
TODO 조건)나이 조건, 알파벳 길이 조건
'''