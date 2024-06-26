# BFS사용을 위한 deque import
from collections import deque


def bfs(V):
    q = deque()
    q.append(V)
    chk_bfs[V] = 1  # 맨처음 좌표 방문
    while q:
        l = q.popleft()  # bfs이기 때문에 popleft로 앞에숫자부터
        ans_bfs.append(l)  # 방문표시
        for i in range(1, N+1):
            # 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하기때문에 1~N+1로 해줌
            if graph[l][i] == 1 and chk_bfs[i] == 0:
                q.append(i)
                chk_bfs[i] = 1  # 큐에 넣고 방문체크해줌. 안하면 숫자가 또들어감


def dfs(V):
    # 양방향이라서 스택으로 바꾸는거 안되는듯..
    chk_dfs[V] = 1 #방문체크 해줌
    ans_dfs.append(V) 
    for i in range(1, N+1):
        if graph[V][i] == 1 and chk_dfs[i] == 0: #연결된 정점은 바로 dfs돌려줌
            dfs(i)


N, M, V = map(int, input().split())

# graph 인덱스를 맞추기위해 N+1 * N+1 로 생성
graph = [[0]*(N+1) for _ in range(N+1)]
# 정답출력 위한 리스트
ans_bfs = []
ans_dfs = []
# 방문 체크표시
chk_bfs = [0]*(N+1)
chk_dfs = [0]*(N+1)
# 양방향이므로 둘다 1표시
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(V)
bfs(V)

print(*ans_dfs)
print(*ans_bfs)
