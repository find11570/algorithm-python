import sys
sys.stdin= open("../input.txt", "r")

n = int(input())
board = [0] * n
visited = [False] * n
result = 0

def nqueen(row):
    global result

    # 모든 퀸을 다 놓았을 때 -> 종료
    if row == n:
        result += 1
        return

    for col in range(n):
        # 현재 위치가 아직 방문되지 않았다면
        if not visited[col]:
            # 현재 위치에 퀸을 배치
            board[row] = col

            if check(row):
                visited[col] = True
                nqueen(row + 1)
                visited[col] = False

def check(n):
    for i in range(n):
        # 현재 퀸이 같은 열 또는 대각선에 있는지 확인 n-i: 행 번호 차이 abs(board[n] - board[i])): 열번호차이
        if(board[n] == board[i] or (n-i) == abs(board[n] - board[i])):
            return False
    return True

# 첫 번째 행부터 퀸을 배치하는 함수를 호출
nqueen(0)

print(result)
