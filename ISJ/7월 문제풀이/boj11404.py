import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = 9999999
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    if cost < graph[v1][v2]:
        graph[v1][v2] = cost

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0 , end =' ')
        else:
            print(graph[i][j] , end =' ')
    print()