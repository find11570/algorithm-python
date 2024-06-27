from collections import deque
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(oneArr, max):
    q = deque()
    for row, col in oneArr:
        vis[row][col] = 0
        q.append((row, col))
    while q:
        cur_x, cur_y = q.popleft()
        # print(f'({cur_x}, {cur_y}) -> ', end='')
        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if vis[nx][ny] != 0 or board[nx][ny] != 0:
                continue
            board[nx][ny] = 1
            vis[nx][ny] = vis[cur_x][cur_y] + 1
            max = vis[nx][ny] if vis[nx][ny] > max else max
            q.append((nx, ny))
    return max


def rotten(arr):
    for i in arr:
        t = i.count(0)
        if t > 0:
            return 1
    return 0

m, n = map(int, input().split())
oneArr = []
board = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    board.append(arr)
    for j in range(0, len(arr)):
        if arr[j] == 1:
            oneArr.append((i, j))

vis = [[0] * m for _ in range(n)]

max = 0
max = bfs(oneArr, max)

rot = rotten(board)
if rot == 1:
    print(-1)
else :
    print(max)
