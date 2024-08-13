from collections import deque
# import java.util.LinkedList;
# import java.util.Queue;
# 자바에서 큐를 사용하려고 할땐 두개.


def solution(maps):
    n, m = len(maps), len(maps[0])
    chk = [[False] * m for _ in range(n)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    def bfs():
        q = deque()
        q.append((0, 0, 1))
        chk[0][0] = True
        while q:
            ny, nx, dist = q.popleft()
            if ny == n - 1 and nx == m - 1:
                return dist
            for i in range(4):
                ey = ny + dy[i]
                ex = nx + dx[i]
                if 0 <= ey < n and 0 <= ex < m and maps[ey][ex] == 1 and not chk[ey][ex]:
                    chk[ey][ex] = True
                    q.append((ey, ex, dist + 1))
        return -1
    return bfs()
