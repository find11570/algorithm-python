# 좋다 # 1253
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort() # 투 포인터 사용을 위해 정렬

count = 0

for i in range(n) :
    start, end = 0, len(arr)-1 # 시작점, 끝점 초기화
    while start < end :
        sum = arr[start] + arr[end]
        if arr[i] == sum :
            # start, end가 i와 겹치지 않도록
            if start != i and end != i :
                count += 1 # 좋은 수
                break
            elif start == i :
                start += 1
            elif end == i :
                end -= 1
        elif arr[i] > sum :
            start += 1
        else : # arr[i] < sum
            end -= 1
print(count)