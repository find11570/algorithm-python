# 숨바꼭질 : 그래프 # 6118

from collections import deque

# 헛간의 개수(n), 연결 정보의 수(m)
n, m = map(int, input().split())

# 각 헛간의 방문 여부를 저장할 리스트와 연결 그래프를 초기화
visited = [-1 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

# 각 헛간 간의 연결 정보를 입력받고 그래프에 저장
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 시작 헛간 1을 0만큼의 비용으로 방문 처리하고 큐에 넣는다.
visited[1] = 0
q = deque()
q.append(1)

# BFS를 사용하여 최단 거리를 계산
while q:
    x = q.popleft()
    for i in graph[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            q.append(i)

# 가장 먼 거리, 해당 거리에 있는 헛간 번호, 그 헛간의 개수를 초기화
dis = 0
target = 0
cnt = 0

# 최대 거리와 그에 해당하는 헛간 번호, 개수를 계산
for i in range(1, n + 1):
    if visited[i] > dis:
        dis = visited[i]
        target = i
        cnt = 1
    elif visited[i] == dis:
        cnt += 1

# 결과 출력
print(target, dis, cnt)