from heapq import *
import sys
INF=sys.maxsize 
input = sys.stdin.readline

V, E = map(int, input().split())
K=int(input())
# 간선 index를 그대로 사용하기 위해 V+1
edge = [[] for _ in range(V+1)]
# 각 거리 무한대로 초기화 
dist=[INF]*(V+1)

# 단방향방향그래프
for _ in range(E):
    u,v,w= map(int, input().split())
    edge[u].append((w, v))

dist[K]=0 # 시작점 가중치 0
heap = [(0,K)] #가중치가 0인 시작노드
while heap:
    w, v = heappop(heap)
    if w!=dist[v]: #같지 않다면 이미 최소치로 수정이 되어있음..
        continue
    for nw,nv in edge[v]:
        if dist[nv]>dist[v]+nw:
            dist[nv]=dist[v]+nw
            heappush(heap,(dist[nv],nv))

for i in range(1,len(edge)):
    if dist[i]==INF:print("INF")
    else:
        print(dist[i])
    
