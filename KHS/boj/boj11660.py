# 구간 합 구하기 5 # 11660
import sys

n, m = map(int, sys.stdin.readline().split()) # n = 표의 크기, m = 계산 횟수

# n x n 의 표 입력
arr = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row)

# 합 배열을 만들기 위해 n+1 x n+1 배열 생성. (1, N), (N, 1)은 모두 0으로 채움
sum_arr = [[0] * (n+1) for _ in range(n+1)]

# 합 배열 생성
for i in range(1, n+1): # 1부터 유효값
    for j in range(1, n+1):
        sum_arr[i][j] = arr[i-1][j-1] + sum_arr[i][j-1] + sum_arr[i-1][j] - sum_arr[i-1][j-1]

# 계산 횟수 m 만큼 구간 합 result 계산
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = sum_arr[x2][y2] - sum_arr[x2][y1-1] - sum_arr[x1-1][y2] + sum_arr[x1-1][y1-1] 
    print(result)