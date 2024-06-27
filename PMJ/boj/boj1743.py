import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt","r")

N, M, K = map(int,input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

count = 0
count_arr = []

for _ in range(K):
    n,m = map(int,input().split())
    graph[n-1][m-1] = 1

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or graph[x][y] == 0:
        return False
    return True

def dfs(x,y):
    global count

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx,dy in zip(dxs,dys):
        new_x, new_y = x+dx, y+dy

        if can_go(new_x,new_y):
            visited[new_x][new_y] = True
            count += 1
            dfs(new_x,new_y)


for i in range(N):
    for j in range(M):
        if can_go(i,j):
            visited[i][j] = True

            count = 1

            dfs(i,j)

            count_arr.append(count)

print(max(count_arr))