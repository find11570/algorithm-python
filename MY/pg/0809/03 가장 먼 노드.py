from collections import deque


def solution(n, edge):
    def bfs(start, cnt):
        q = deque()
        q.append([start, cnt])

        while q:
            start, cnt = q.popleft()
            chk[start] = cnt
            visited[start] = True
            for j in range(len(graph[start])):
                if visited[graph[start][j]] == False:
                    visited[graph[start][j]] = True
                    q.append([graph[start][j], cnt+1])

    graph = [[] for _ in range(n+1)]
    chk = [0]*(n+1)
    visited = [False]*(n+1)

    for i in range(len(edge)):
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])
    bfs(1, 0)
    answer = chk.count(max(chk))
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
