# 최소 스패닝 트리 : MST # 1197

import sys

input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())  # 정점(V)과 간선(E)의 개수 입력받기

edges = []
for _ in range(E):
    A, B, C = map(int, input().split())  # 각 간선의 두 정점(A, B)과 비용(C) 입력받기
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2])  # 비용(C)이 적은 순서대로 간선 정렬

# 유니온-파인드(Union-Find) 자료구조
parent = [i for i in range(V+1)]  # 부모 테이블 초기화: 각 노드의 부모를 자기 자신으로 설정

def get_parent(x):
    if parent[x] == x:  # 부모가 자기 자신인 경우
        return x
    parent[x] = get_parent(parent[x])  # 부모를 찾을 때까지 재귀적으로 호출하고, 경로 압축(Path Compression) 수행
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:  # 더 작은 숫자의 노드를 부모로 설정
        parent[b] = a
    else:
        parent[a] = b        

def same_parent(a, b):
    return get_parent(a) == get_parent(b)  # 두 노드가 같은 부모를 가지는지 확인

answer = 0
for a, b, cost in edges:
    # 비용이 작은 간선부터 하나씩 추가하면서 사이클이 발생하지 않을 때만 선택
    if not same_parent(a, b):
        union_parent(a, b)
        answer += cost
print(answer)  # 최소 스패닝 트리의 전체 비용 출력