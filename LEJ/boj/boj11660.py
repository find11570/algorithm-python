# 백준
# 11660 : 구간 합 구하기 5(실버 1)
##############################################################

import sys

n,m = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] -dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    result = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)
    