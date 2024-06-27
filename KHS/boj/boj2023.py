# 신기한 소수 # 2023
import sys, math

n = int(sys.stdin.readline())

def isPrime(x): # 소수인지 판별하는 함수
    for i in range(2, int(math.sqrt(x)) + 1): # n / 2 시간 초과
        if int(x) % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1, 10, 2): # 홀수일때만
            temp = num * 10 + i
            if isPrime(temp): # 소수이면 dfs
                dfs(temp)

# 한 자리 소수로 부터 탐색 시작
dfs(2)
dfs(3)
dfs(5)
dfs(7)
