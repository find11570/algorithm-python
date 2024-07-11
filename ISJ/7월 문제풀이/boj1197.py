import sys
import heapq

input = sys.stdin.readline

n , v= map(int, input().split())

INF = 9999999
graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(v):
    v1, v2, c = map(int, input().split())
    graph[v1].append((c, v2))
    graph[v2].append((c, v1))

answer = 0
visited = [False] * (n+1)
min_heap = [(0,1)]

while min_heap:
    cost, node = heapq.heappop(min_heap)
    if visited[node]:
        continue
    visited[node] = True
    answer += cost

    for vertex, neighbor in graph[node]:
        if not visited[neighbor]:
            heapq.heappush(min_heap, ([vertex, neighbor])

print(answer)
