# import sys

# # 입력
# n, m = map(int, sys.stdin.readline().split())
# lst = list(map(int, sys.stdin.readline().split()))

# start, end = 1, max(lst)  # 초기 시작과 끝 값 설정

# while start <= end:
#     sum = 0
#     mid = (start + end) // 2  # 중간값 설정

#     for l in lst:
#         if l > mid:
#             sum += l - mid  # 중간값을 기준으로 잘랐을 때 가져갈 수 있는 나무 길이 합 계산
    
#     if sum < m:  # 가져갈 수 있는 나무 길이 합이 목표보다 작은 경우
#         end = mid - 1  # 높이를 낮춰야 함
#     else:  # 가져갈 수 있는 나무 길이 합이 목표보다 크거나 같은 경우
#         start = mid + 1  # 높이를 높여야 함


# print(end)  # 결과 출력
n, m = map(int, input().split())  
trees = list(map(int, input().split()))  

def binary_search(trees, target):
    left, right = 0, max(trees)  # 이분 탐색을 위해 시작 위치와 끝 위치를 지정

    while left <= right:  # 시작 위치가 끝 위치를 넘지 않을 때까지 반복
        mid = (left + right) // 2  # 중간 위치
        total = 0  # 자른 나무의 길이를 합산할 변수 초기화
        for h in trees: 
            if h > mid:  # 현재 위치보다 높이가 높은 나무만 자를 수 있음
                total += h - mid  # 자른 나무의 길이를 합산

        if total < target:  # 합산된 자른 나무의 길이가 가져가려는 길이보다 작으면
            right = mid - 1  # 자를 위치를 더 위쪽으로 이동하여 나무의 길이를 더 높임
        else:
            left = mid + 1  # 자를 위치를 더 아래쪽으로 이동하여 나무의 길이를 더 낮춤

    return right  # 가져갈 수 있는 가장 긴 나무의 길이를 반환

print(binary_search(trees, m))