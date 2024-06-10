import sys
import heapq

arr = []
q = heapq # heapq 선언
N = int(sys.stdin.readline()) # N 입력 받음
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        q.heappush(arr, (abs(num), num)) # 절대 값으로 우선순위를 정해서 값을 넣어준다
    elif num == 0:
        if len(arr) == 0: # list의 길이가 0일때의 예외 처리
            print(0)
            continue
        print(q.heappop(arr)[1]) # list에 값이 들어가 있다면 절대값 우선순위로 들어간 값들 출력

