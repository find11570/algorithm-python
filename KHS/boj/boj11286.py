# 절댓값 힙 # 11286
import sys, heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        # 힙에 (절댓값, 원래 값)을 튜플로 저장
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap:
            # 절댓값이 가장 작은 값을 출력하고 제거
            print(heapq.heappop(heap)[1])
        else:
            print(0)