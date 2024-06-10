import sys

N = int(sys.stdin.readline().rstrip())
towers = list(map(int, sys.stdin.readline().split()))
stack = [] # 조건에 맞는 탑들 저장할 stack
answer = [0] * N # 수신한 탑들의 주소 저장할 list
for i in range(N-1, -1, -1):
    if len(stack) == 0: # 전파를 쏘는 탑이 없으면 stack에 현재 전파탑의 인덱스 저장
        stack.append(i)
    elif towers[stack[-1]] > towers[i] : # 현재 탑보다 먼저쏘고 있는 이전 전파탑이 더 높은 경우에도 stack에 저장
        stack.append(i)
    else:
        while len(stack) > 0 and towers[stack[-1]] <= towers[i] : # 현재탑이 이전탑보다 높은 경우 stack에 저장된 인덱스들을 pop해주면서 현재탑의 인덱스를 정답 list에 저장
            answer[stack[-1]] = i+1
            stack.pop()
        stack.append(i)

[print(i, end = ' ') for i in answer]
