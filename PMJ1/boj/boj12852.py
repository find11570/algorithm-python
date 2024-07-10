target = int(input())
dp = [0] * (target + 1) # 횟수를 저장하는 list
answer = [0] * (target + 1) # dp의 idx를 저장한다. 예를 들어 4의 횟수를 구할때
# 여기 알고리즘에서는 4 3 1로 구해진다 
# 4의 횟수를 구할 때 dp[3]에서 +1 한 값을 저장했으므로 answer[4] = 3이 되는식!
# 기본 개념은 dp의 idx에 구하고자 하는 값의 횟수를 저장하고 1을빼거나, 3으로 나누거나 2로나눈 수 중
# 횟수가 가장적은 수에 +1을 해서 dp에 저장한다.
for i in range(2, target + 1): # 0과 1은 0이므로 2부터 시작한다.
    dp[i] = dp[i - 1] + 1 # 먼저 -1을 했을때의 dp저장소에서 값을 가져온다.
    answer[i] = i - 1 
    if i % 2 == 0 and dp[i // 2] < dp[i] - 1: # 만일 2로나누어 떨어지고 i/2에 저장되어 있는 값이 -1때의 값보다 작다면 변경한다.
        dp[i] = dp[i // 2] + 1
        answer[i] = i // 2
    if i % 3 == 0 and dp[i // 3] < dp[i] - 1: # 2로 나눌때와 개념은 같지만 elif가 아닌 if로 들어가야한다. 6의 배수의 경우를 고려해야 하기 때문
        dp[i] = dp[i // 3] + 1
        answer[i] = i // 3
print(dp[target])
print(target, end=' ')
while answer[target] != 0:
    print(answer[target], end=' ')
    target = answer[target]
