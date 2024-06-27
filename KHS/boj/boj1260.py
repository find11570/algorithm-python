# DFS와 BFS # 1260

# DFS -> 재귀로 구현 
# BFS -> while, deque로 구현
import sys
n, m, v = map(int, sys.stdin.readline().split())

#행렬 만들기
graph = [[0] * (n + 1) for _ in range(n + 1)] # 리스트 컴프리헨션
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

#방문 리스트 행렬
visited_dfs = [0]*(n + 1)
visited_bfs = visited_dfs.copy()

#dfs 함수 만들기
def dfs(v):
    visited_dfs[v] = 1 # 방문처리
    print(v, end=' ')
    for i in range(1, n + 1):
        if graph[v][i] == 1 and visited_dfs[i] == 0: # 방문 기록이 없을 때
            dfs(i)

def bfs(v):
    queue = [v]
    visited_bfs[v] = 1 # 방문처리
    while queue:
        v = queue.pop(0) # 방문 노드 제거
        print(v, end = ' ')
        for i in range(1, n + 1):
            if(visited_bfs[i] == 0 and graph[v][i] == 1):
                queue.append(i) # queue에 넣고
                visited_bfs[i] = 1 # 방문처리

dfs(v)
print()
bfs(v)