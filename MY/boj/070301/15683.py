N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = []  # 각 경우의 수 거르기
chk = [[0]*N for _ in range(M)]
cctvs = [[] for _ in range(6)]

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def sol(y,x):
    for i in range(4):
        graph[i]=graph[:]
        ey=y+dy[i]
        ex=x+dx[i]
        for j in range(graph[ey]):
            graph[ey][ex]="#"



for i in range(N):
    for j in range(M):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctvs[graph[i][j]].append((i, j))

for i in range(len(cctvs)):
    for j in range(len(cctvs[i])):
        a, b = cctvs[i][j]
        sol(a,b)

