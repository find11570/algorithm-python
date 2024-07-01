from collections import deque
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(row, col):
    q = deque()
    vis[row][col] = 1
    q.append((row, col))
    while q:
        cur_x, cur_y = q.popleft()
        # print(f'({cur_x}, {cur_y}) -> ', end='')
        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if vis[nx][ny] != 0 or board[nx][ny] != '1':
                continue
            vis[nx][ny] = vis[cur_x][cur_y] + 1
            q.append((nx, ny))



n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))
vis = [[0] * m for _ in range(n)]


bfs(0,0)
print(vis[n-1][m-1])