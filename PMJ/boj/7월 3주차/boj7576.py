import sys
from collections import deque

sys.stdin= open("../input.txt", "r")

n,m = map(int,input().split())

# 토마토 상자 받기
box = [list(map(int,input().split())) for _ in range(m)]

dxs, dys = [1,0,-1,0],[0,1,0,-1]


# 범위 내에 있고 익지 않은 토마토만 익을 수 있어요
def can_go(x,y):
    return 0<=x<m and 0<=y<n and box[x][y]==0

def bfs():
    q = deque()

    # 익은 토마토들을 모두 큐에 넣어줘요
    for i in range(m):
        for j in range(n):
            if box[i][j] == 1:
                q.append((i, j))

    while q:
        a,b = q.popleft()
        for dx,dy in zip(dxs,dys):
            new_x, new_y = a + dx, b + dy
            if can_go(new_x,new_y):
                box[new_x][new_y] = box[a][b] + 1
                q.append((new_x,new_y))


bfs()

max_days = 0
Flag = True
for i in range(m):
    for j in range(n):
        if box[i][j] == 0:
            Flag = False
        else:
            max_days = max(max_days,box[i][j]-1)

if(Flag): print(max_days)
else: print(-1)