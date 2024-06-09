import heapq
import sys

N = int(input())

heap = [] #우선순위 큐, 트리 기반 자료구조


for i in range(N): 
    value = int(sys.stdin.readline())
    if value != 0:
        heapq.heappush(heap, (abs(value), value)) #튜플 (abs(value), value)가 힙에 들어가고 abs(value)를 통해서 정리된다
    else:
        if len(heap) == 0:
            print(0)
        else:
            _,value = heapq.heappop(heap)
            #value = heapq.heappop(heap)[1]도 가능
            print(value)