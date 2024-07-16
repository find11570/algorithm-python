from collections import deque
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

#방문하지 않은 cell 체크
chk = [[-1]*M for _ in range(N)] 
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    q=deque()
    # 출발점이 꼭 0,0부터가 아니라 1인 지점 모두 동시시작해야 하므로 
    # 큐에 동시에 1인지점을 다 넣어줌.
    for y in range(N):
        for x in range(M):
            if graph[y][x]==1:
                q.append((y,x,0))
                chk[y][x]=0
    
    while q:
        ey,ex,ez=q.popleft() #새로 익은 토마토 지점 과 걸렸던 시간
        for i in range(4):
            ny = ey+dy[i]
            nx = ex+dx[i]
            # 방문하지않은 지점중 익지 않은 토마토일때
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0 and chk[ny][nx]==-1:
                graph[ny][nx] = 1 # 익게해주고
                q.append([ny,nx,ez+1]) #걸린시간 +1 까지 append
                chk[ny][nx]=(ez+1) # 걸린 시간

bfs()
max_days=0
for i in range(N):
    for j in range(M):
        if graph[i][j]==0: #익지 않은 토마토 있으면 -1 출력 후 종료 
            print(-1)
            exit()
        max_days=max(max_days,chk[i][j])

print(max_days)