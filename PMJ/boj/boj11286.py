import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if (x!=0):
        heappush(heap,(abs(x), x))
    else:
        if (heap):
            print(heappop(heap)[1])
        else:
            print(0)
