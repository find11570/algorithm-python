import sys
import heapq

input = sys.stdin.readline

V,E= map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

INF = 99999999
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))

q = []
heapq.heappush(q, (0, K))
distance[K] = 0;

while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
        continue

    for next_node , weight in graph[node]:
        current = dist + weight
        if current <  distance[next_node]:
            distance[next_node] = current
            heapq.heappush(q, (current, next_node))


for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])