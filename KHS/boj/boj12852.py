# 1로 만들기 2 # 12852

n = int(input())

# dp 테이블 초기화: 각 인덱스는 인덱스 자체로 초기화 (예: dp[3] = 3)
dp = [i for i in range(n + 1)]
dp[1] = 0 # dp[1]은 0으로 초기화 (1은 이미 최단 경로임)

# 정답을 저장할 리스트 초기화
answer = [i for i in range(n + 1)]
answer[1] = 0

# 2부터 n까지의 숫자를 대상으로 dp 값 계산
for i in range(2, n + 1):
    # 이전 숫자에서 1을 더한 것이 현재 숫자가 되는 경우
    dp[i] = dp[i - 1] + 1
    answer[i] = i - 1
    
    # 현재 숫자가 3으로 나누어 떨어지고, 3으로 나눈 숫자에서 1을 더한 값이 더 작은 경우
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        answer[i] = i // 3

    # 현재 숫자가 2로 나누어 떨어지고, 2로 나눈 숫자에서 1을 더한 값이 더 작은 경우
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        answer[i] = i // 2

# 최단 경로의 최소 연산 횟수 출력
print(dp[n])

# n에서 1까지 가는 경로 출력
print(n, end=" ")

target = n
# 역추적을 통해 경로를 출력
while answer[target] != 0:
    print(answer[target], end=" ")
    target = answer[target]