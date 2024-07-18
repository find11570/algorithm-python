# 1. 각 cctv 타입마다 방향의 조합을 미리 cctv 배열로 생성.
# - type : 1~5

# - direction : 0~3

# - direction -> 0 : 상, 1 : 우, 2 : 하, 3 : 좌

# dx와 dy도 direction 순서에 맞게 셋팅

 

# board를 탐색하며 모든 cctv의 좌표를 cctv_loc 배열에 저장. 이 때, cctv_type도 함꼐 저장
 

# 재귀로 모든 경우를 탐색한다. 파라매터는 현재까지 탐색한 cctv의 개수
# 현재까지 탐색한 cctv의 개수인 curr_cnt가 cctv의 총 개수인 cctv_cnt와 같다면 사각지대의 수를 세고 answer를 최솟값으로 갱신한 후 함수 종료.
# 각 cctv의 좌표에서 탐색 시작. cctv의 타입에 따른 모든 경우의 수와, 각 경우에 해당하는 모든 방향에 대해 일직선으로 탐색
# 이 때, board를 deepcopy하지 않기 위해 reset배열을 사용. 변화시킨 board의 요소들의 좌표와 초깃값을 저장하여 재귀호출 이후 리셋해준다. (이 방법은 deepcopy를 사용하는 것보다 시간적으로 효율적이다. 그러나 변화시킨 좌표가 커지면 메모리 사용량이 크게 늘어나기 때문에 상황에 맞게 적절히 사용하는 것이 중요하다.)
# curr_cnt에 1을 더하여 다음 cctv 탐색을 재귀호출하고 1번부터 반복

import sys
input = sys.stdin.readline

cctv = [
    [], # 각 CCTV가 바라볼 방향
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = float("inf") #무한대로 초기화 
N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
cctv_loc = []
cctv_cnt = 0

# CCTV 좌표 확인
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctv_cnt += 1
            cctv_loc.append([i,j, board[i][j]]) # cctv 좌표와 타입 저장

# 모든 CCTV 죄표의 모든 방향의 경우를 확인
def dfs(curr_cnt):
    global cctv_cnt, answer
    ans_cnt = 0

    if curr_cnt == cctv_cnt: # 모든 cctv를 다 확인한 경우
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0: # 사각지대 개수 카운트
                    ans_cnt += 1 
        answer = min(answer,ans_cnt)
        return

    cctv_dx = cctv_loc[curr_cnt][0] # cctv의 x좌표
    cctv_dy = cctv_loc[curr_cnt][1] # cctv의 y좌표
    cctv_type = cctv_loc[curr_cnt][2] # cctv의 타입(번호) range 1 ~ 5
    for cctv_dir in cctv[cctv_type]: # cctv의 타입에서 가능한 모든 방향의 조합읉 탐색
        reset = [] # deepcopy를 사용하지 않기 위해 원래상태로 복구할 좌표를 담을 list
        for d in cctv_dir: # 각 타입의 모든 방향으로 탐색
            ax = cctv_dx
            ay = cctv_dy
            while True:
                ax += dx[d]
                ay += dy[d]
                if 0 <= ax < N and 0 <= ay < M and board[ax][ay] != 6: # 벽이 아니고 사무실을 벗어나지 않을 때
                    reset.append([ax,ay,board[ax][ay]]) # board를 원상복구시키기 위한 배열에 삽입
                    board[ax][ay] = 7 
                else:
                    break
        dfs(curr_cnt + 1) # 다음 cctv 좌표 확인
        for x,y,type in reset: # 탐색한 좌표들을 다시 원상복구해야 다음번 탐색이 독릭접으로 실행될 수 있음
            board[x][y] = type
dfs(0)
print(answer)