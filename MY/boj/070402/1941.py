import sys
from collections import deque

input = sys.stdin.read

# 입력된 문자열을 행별로 나누어 grid에 저장
grid = [list(row) for row in input().split()]
# 선택된 위치를 저장할 리스트
position = []

# 4방향 탐색을 위한 배열 (우, 좌, 하, 상)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 선택된 위치들이 서로 연결되어 있는지 확인하는 함수
def connected(position):
    # 큐를 사용하여 BFS를 수행
    q = deque([position[0]])
    # 방문한 위치를 저장하기 위한 집합
    visited = set([position[0]])
    count = 1

    while q:
        x, y = q.popleft()
        # 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 새로운 위치가 position에 있고, 아직 방문하지 않았다면
            if (nx, ny) in position and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
                count += 1
    # 방문한 위치의 수가 7개여야 모든 위치가 연결된 것
    return count == 7

# 백트래킹을 통해 가능한 조합을 찾는 함수
def backtracking(start, S, count):
    global answer

    # 7개의 위치를 모두 선택한 경우
    if count == 7:
        # 선택된 위치가 연결되어 있고, 'S'가 4개 이상인 경우
        if S >= 4 and connected(position):
            answer += 1
        return

    # 25개의 위치를 하나씩 확인
    for i in range(start, 25):
        x = i // 5
        y = i % 5
        # 현재 위치를 선택된 위치에 추가
        position.append((x, y))
        # 현재 위치의 값이 'S'인 경우
        if grid[x][y] == 'S':
            backtracking(i + 1, S + 1, count + 1)
        else:
            backtracking(i + 1, S, count + 1)
        # 현재 위치를 선택된 위치에서 제거
        position.pop()

# 정답을 저장할 변수 초기화
answer = 0
# 백트래킹 함수 호출
backtracking(0, 0, 0)
# 결과 출력
print(answer)
