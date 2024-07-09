# 플로이드 : 플로이드-워셜 # 11404

INF = int(1e9)  # 무한대 값 설정

# 도시(vertex)의 개수, 버스(edge)의 개수
N = int(input())
M = int(input())

# 그래프 초기화. 최단 거리를 저장할 2차원 배열을 INF(무한대)로 초기화.
graph = [[INF] * (N+1) for _ in range(N+1)]

# 자기 자신으로 가는 경로는 비용이 0
for i in range(1, N+1):
    graph[i][i] = 0

# 각 간선에 대한 정보를 입력받아 그래프에 최신화.
for _ in range(M):
    a, b, c = map(int, input().split())
    # 동일 경로에서 비용이 최소값으로 설정되도록 갱신.
    graph[a][b] = min(graph[a][b], c)

# 플로이드-워셜 알고리즘 모든 노드 간의 최단 경로를 계산.
for k in range(1, N+1):  # 경유지
    for a in range(1, N+1):  # 출발지
        for b in range(1, N+1):  # 도착지
            # 직접 가는 경로와 경유지를 거쳐 가는 경로 중 더 작은 비용으로 갱신
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for x in range(1, N+1):
    for y in range(1, N+1):
        if graph[x][y] == INF:
            print(0, end=' ')  # 도달할 수 없는 경우 0 출력
        else:
            print(graph[x][y], end=' ')  # 최단 경로 비용 출력
    print()  # 줄 바꿈
