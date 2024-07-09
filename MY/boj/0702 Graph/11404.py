import sys
input=sys.stdin.readline
INF=sys.maxsize
# Dijkstra -> 1e8 시간 초과 가능성
# Floyd -> 1e6 가능 O(V^3)
# 모든점에서 모든점 -> 플로이드 이용함
#
N=int(input())
m=int(input())
rs=[[INF]*(N+1) for _ in range(N+1)]

# 출발노드와 도착노드가 같을때 
for i in range(1, n+1):
    rs[i][i] = 0

for i in range(m):
    a,b,c = map(int, input().split())
    # 맨처음부터 초기값이 INF로 되어있고 c가 더작기 때문에 최소로 min이 와야함
    rs[a][b] = min(rs[a][b], c)

for k in range(1, n+1): # 거치는 값
    for j in range(1, n+1): # 시작점
        for i in range(1, n+1): # 도착점
            if rs[j][i] > rs[j][k] + rs[k][i]:
                rs[j][i] = rs[j][k] + rs[k][i]

for j in range(1, n+1):
    for i in range(1, n+1):
        if rs[j][i] == INF: print(0, end=' ')
        else: print(rs[j][i], end = ' ')
    print()