from heapq import *
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
# index를 그대로 사용하기 위해 V+1
edge = [[] for _ in range(V+1)]
# 노드 방문체크
chk = [False]*(V+1)

# edge가 양방향이므로 A,B둘다 append (가중치,노드)
for _ in range(E):
    A, B, C = map(int, input().split())
    edge[A].append((C, B))
    edge[B].append((C, A))
# 결과값 0부터
rs = 0
heap = [(0, 1)]
while heap:
    w, next_node = heappop(heap)
    if chk[next_node] == False:
        chk[next_node] = True
        rs += w
        for next_edge in edge[next_node]:
            #(가중치,노드)
            # next_edge[1]==노드
            if chk[next_edge[1]] == False:
                #(3,2)가 있는 상태에서 (2,3)이 push됨.
                heappush(heap, next_edge)
print(rs)
