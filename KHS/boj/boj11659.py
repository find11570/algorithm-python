# 구간 합 구하기 4 # 11659
import sys

n, m = map(int, sys.stdin.readline().split()) # n = 수의 개수, m = 합을 구해야하는 횟수

arr = map(int, sys.stdin.readline().split()) # n개의 수
sum = 0
sum_arr = [0] # sum_arr[0] = 0으로 초기화 생성

# 합 배열 구하기
for i in arr :
    sum += i
    sum_arr.append(sum)

for _ in range(m) :
    i, j = map(int, sys.stdin.readline().split()) # 합을 구해야 하는 구간 i, j
    print(sum_arr[j]-sum_arr[i-1])