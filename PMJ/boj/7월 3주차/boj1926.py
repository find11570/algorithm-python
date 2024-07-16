import sys
from collections import deque

sys.stdin= open("../input.txt", "r")

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dxs,dys = [0, 0, 1, -1], [1, -1, 0, 0]
def can_go(x,y):
    return 0<=x<n and 0<=y<m and not visited[x][y] and graph[x][y]==1

def bfs(x,y):
    count = 1

    q = deque()
    q.append((x,y))

    while q:
        a,b = q.popleft()

        for dx,dy in zip(dxs,dys):
            new_x, new_y = a+dx, b+dy

            if can_go(new_x,new_y):
                count += 1
                visited[new_x][new_y] = True
                q.append((new_x,new_y))

    return count

arr = []

for i in range(n):
    for j in range(m):
        if can_go(i,j) :
            visited[i][j] = True
            arr.append(bfs(i,j))


if len(arr) == 0:
    print(len(arr))
    print(0)
else:
    print(len(arr))
    print(max(arr))
