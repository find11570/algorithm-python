from collections import deque
import sys


def dfs(graph, start, visit):
    visit[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visit[i]:
            visit[i] = True
            dfs(graph, i, visit)


def bfs(graph, start, visit):
    queue = deque()
    queue.append(start)
    visit[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True

n, m, start = map(int, sys.stdin.readline().split())
graph = []
visitDFS = [False] * (n + 1)
visitBFS = [False] * (n + 1)
for i in range(0, n + 1):
    graph.append([])

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs(graph, start, visitDFS)
print("")
bfs(graph, start, visitBFS)