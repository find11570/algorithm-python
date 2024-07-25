import sys

# 입력
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(lst)  # 초기 시작과 끝 값 설정

while start <= end:
    sum = 0
    mid = (start + end) // 2  # 중간값 설정

    for l in lst:
        if l > mid:
            sum += l - mid  # 중간값을 기준으로 잘랐을 때 가져갈 수 있는 나무 길이 합 계산
    
    if sum < m:  # 가져갈 수 있는 나무 길이 합이 목표보다 작은 경우
        end = mid - 1  # 높이를 낮춰야 함
    else:  # 가져갈 수 있는 나무 길이 합이 목표보다 크거나 같은 경우
        start = mid + 1  # 높이를 높여야 함

print(end)  # 결과 출력
