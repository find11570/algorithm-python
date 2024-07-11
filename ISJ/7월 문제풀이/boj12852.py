import sys

input = sys.stdin.readline
num = int(input())

if num < 1:
    print(0)
    print(1)

dp = [0] * (num + 1)
lst = [0] * (num + 1)

for i in range(2, num + 1):
    dp[i] = dp[i - 1] + 1
    lst[i] = i - 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        lst[i] = i // 2

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        lst[i] = i // 3

print(dp[num])

sequence = []
while num > 0:
    sequence.append(num)
    num = lst[num]


for i in sequence:
    print(i, end=' ')