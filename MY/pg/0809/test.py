from collections import deque
def solution(n, edge):
    def bfs(start,cnt):
        q=deque()
        visited[start]=True
        q.append([start,cnt])
        while q:
            start,cnt=q.popleft()
            answer[start]=cnt
            for j in range(len(graph[start])):
                if visited[graph[start][j]]==False:
                    visited[graph[start][j]]=True
                    q.append([graph[start][j],cnt+1])
                    
    graph=[[] for _ in range(n+1)]
    for i in range(len(edge)):
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])
    visited=[False]*(n+1)
    answer = [0]*(n+1)
    bfs(1,0)
    
    return answer.count(max(answer))