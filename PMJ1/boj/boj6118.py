import sys
import heapq
from collections import deque


def bfs(start, graph, dq, mst):
    dq.append((start, 0))
    vis.add(start)
    while dq:
        node, cnt = dq.popleft()
        for i in graph[node]:
            if i in vis:
                continue
            dq.append((i, cnt + 1))
            vis.add(i)
            heapq.heappush(mst, (i, cnt + 1))


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
vis = set()
mst = []
dq = deque()
cnt = 0

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

bfs(1, graph, dq, mst)
mst.sort(key=lambda x: (x[1], -x[0]))
idx, maxVal = mst.pop()
answer = 1
while mst:
    val = mst.pop()[1]
    if maxVal != val:
        break
    answer += 1
print(idx, maxVal, answer)
