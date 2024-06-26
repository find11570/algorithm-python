from collections import deque
import sys
input = sys.stdin.readline

#dfs 상하좌우
dy=[-1,1,0,0]
dx=[0,0,-1,1]

def dfs(y,x):
    stk=[]
    stk.append((y,x))
    #스택으로 dfs사용
    #발견한 배추의 인접배추 찾기
    while stk:
        ey,ex=stk.pop()
        for i in range(4):
            ny=ey+dy[i]
            nx=ex+dx[i]

            if 0<=ny<N and 0<=nx<M:
                if visit[ny][nx]==False and graph[ny][nx]==1:
                    #조건에 맞으면 스택에 삽입
                    visit[ny][nx]=True #방문체크
                    stk.append((ny,nx))

T = int(input())
for test_case in range(T):
    M, N, K = map(int, input().split()) #가로 세로 지렁이개수
    graph = [[0]*M for _ in range(N)] #배추밭 그래프
    visit = [[False]*M for _ in range(N)]
    cnt=0 #지렁이갯수
    # 배추좌표
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if visit[i][j]==False and graph[i][j]==1:
                visit[i][j]=True
                cnt+=1 #배추발견하면 +1
                dfs(i,j)
    print(cnt)