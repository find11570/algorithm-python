import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
# 그래프 생성
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

# BFS 생성
distance = [-1] * (N + 1)
distance[1] = 0
queue = deque([1])

while queue:
    vertex = queue.popleft()

    for neighbor in graph[vertex]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[vertex] + 1
            queue.append(neighbor)

vertex_length = max(distance[1:])
index = 1

for i in range(1, N + 1):
    if distance[i] == vertex_length:
        index =i
        break

same = 0

for dist in distance:
    if vertex_length == dist:
        same += 1
print(index, vertex_length, same)