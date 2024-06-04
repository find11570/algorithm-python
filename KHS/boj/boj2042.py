# 구간 합 구하기 # 2042
# unsolved : 시간 초과 => 세그먼트 트리로 해결해야 함.
import sys
# n = 수의 개수, m = 수의 변경이 일어나는 횟수, k = 구간의 합 구하는 횟수
n, m, k = map(int, sys.stdin.readline().split()) 

# 수 입력. 1차원 배열 생성
arr = []
for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)

# 이벤트 발생
for _ in range(m+k): # 모든 이벤트 횟수의 합 만큼 반복
    row = list(map(int, sys.stdin.readline().split()))
    if row[0] == 1 : # m, 수 변경 이벤트일 때
        arr[row[1]-1] = row[2]
        # print("1", arr) # 검산
    elif row[0] == 2 : # k, 구간의 합 이벤트일 때
        sum = 0
        sum_arr = []
        for i in arr :
            sum += i
            sum_arr.append(sum)
        # print(sum_arr, sum_arr[row[2]-1],"-",sum_arr[row[1]-2]) # 검산
        result = sum_arr[row[2]-1] - sum_arr[row[1]-2] 
        print(result)
        