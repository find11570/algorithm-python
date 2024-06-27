import sys
sys.stdin = open("input.txt","r")
from collections import deque

N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    for i in sorted(graph[node]):
        if not visited[i]:
            print(i,end=" ")
            visited[i] = True
            dfs(i)

print(V,end=" ")
visited[V] = True
dfs(V)
print()

visited2 = [False for _ in range(N+1)]
bfs_arr= []

def bfs():
    while(q):
        node = q.popleft()
        print(node,end=" ")

        for i in sorted(graph[node]):
            if not visited2[i]:
                q.append(i)
                visited2[i] = True

q = deque()
q.append(V)
visited2[V] = True
bfs()

