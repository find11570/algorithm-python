import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    # 가중치 0, 시작노드
    q.append([0, start])
    chk[start] = 1
    while q:
        dist, y = q.popleft()
        # 시작노드의 가중치는 0
        ans[y] = dist
        for j in graph[y]:
            if chk[j] == 0:
                # 시작노드 에 붙어있는 노드들은 기존 가중치 +1
                q.append([dist+1, j])
                chk[j] = 1


# 노드 N, 간선 M
N, M = map(int, input().split())
# 방문노드 체크
chk = [0]*(N+1)
graph = [[] for _ in range(N+1)]

# 인접리스트 활용
for _ in range(M):
    A_i, B_i = map(int, input().split())
    graph[A_i].append(B_i)
    graph[B_i].append(A_i)

ans = [0]*(N+1)
bfs(1)
print(ans.index(max(ans)), max(ans), (ans.count(max(ans))))
