import sys
from collections import deque

def BFS(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for neighbor in sorted(graph[node]):
                if neighbor not in visited:
                    queue.append(neighbor)
            
def DFS(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for neighbor in sorted(graph[node], reverse=True):
                if neighbor not in visited:
                    stack.append(neighbor)


input = sys.stdin.read
data = input().split()

# Read N, M, V
N, M, V = map(int, data[:3])

graph = {i: [] for i in range(1, N + 1)}

index = 3
for _ in range(M):
    a = int(data[index])
    b = int(data[index + 1])
    graph[a].append(b)
    graph[b].append(a)
    index += 2
    
DFS(graph, V)
print()
BFS(graph, V)
