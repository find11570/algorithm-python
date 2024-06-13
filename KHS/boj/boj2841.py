# 외계인의 기타 연주 # 2841
import sys

N, P = map(int, input().split()) # N: 총 음의 수, P: 각 줄의 최대 플랫 수
stack = [[] for _ in range(7)] # 줄 6개
count = 0

for i in range(N): # 각 음을 입력받아 처리
    n, p = map(int, sys.stdin.readline().split()) # n: 현재 줄 번호, p: 현재 플랫 번호
    # 줄의 스택이 비어있지 않고, p가 스택의 최상단보다 작을 때
    while stack[n-1] and p < stack[n-1][-1]:
        stack[n-1].pop() # 떼기
        count += 1
    # 현재 줄의 스택이 비어있거나 p가 스택의 최상단보다 클 때
    if not stack[n-1] or p > stack[n-1][-1]:
        stack[n-1].append(p) # 누르기
        count += 1
print(count)