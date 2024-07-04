import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 동전 수, 가치
arr = [int(input()) for _ in range(n)]  # 동전 가격 입력

count = 0  # 필요한 동전 수
i = n-1  # arr 마지막 부터 탐색

while i >= 0:
    if k >= arr[i]:  # 필요한 가치 수 보다 동전의 가치가 낮으면
        k -= arr[i]  # 가치 - 동전
        count += 1  # 동전 수 +1
    else:
        i -= 1  # 동전의 가치가 더 높으면 가치가 낮은 다음 동전 탐색/

print(count)
