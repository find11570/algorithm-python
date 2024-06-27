# 트리 # 1068
import sys

n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split())) 
delete = int(sys.stdin.readline())

def dfs(del_node):
    tree[del_node] = -2 # 제거
    for i in range(n):
        if del_node == tree[i]: # tree[i]가 del_node의 자식이면 재귀를 통해 삭제
            dfs(i)
dfs(delete)
cnt = 0
for i in range(n):
    if tree[i] != -2 and i not in tree: # 제거된 노드가 아니고 i의 자식이 없다면
        cnt += 1

print(cnt)