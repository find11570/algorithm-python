import sys
N = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

cnt = 1 # list에 들어갈 오름차순 값
answer = '' # 정답 문자열 저장할 변수
chk = True # NO 인 경우 answer 출력하지 않도록 확인하는 변수
stack = [] # 오름차순 저장할 list
for i in nums:
    while cnt <= i: # 현재 숫자까지 오름차순으로 숫자 저장 및 '+' 문자열 저장 반복문
        stack.append(cnt)
        answer += '+\n'
        cnt += 1

    if i == stack[-1]: # 수열의 숫자와 같으면 stack변수에서 제거뒤 '-' 문자열 저장
        stack.pop()
        answer += '-\n'

    if len(stack) > 0 and stack[-1] > i: # 오름차순으로 저장하고 있으므로 stack에 저장된 값이 수열의 숫자 보다 크면 입력된 수열을 만들수 없음
        print('NO')
        chk = False
        break

if chk:
    print(answer)
