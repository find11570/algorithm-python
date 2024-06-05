# 백준
# 10986 : 나머지 합(골드 3)
##############################################################

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

r = [0] * m # m으로 나눈 나머지 담는 곳

prefixSum = 0

# 누적합을 m으로 나눈 것을 저장할 배열 = r
for i in range(n):
    prefixSum += arr[i]
    r[prefixSum % m] += 1

ans = r[0] # 나머지가 0이 되는 경우의 수
# print(r)
for i in range(m):
    # nC2 = n(n-1)/2
    # 조합으로 풀어야 함!
    ans += r[i] * (r[i]-1) // 2
print(ans)

