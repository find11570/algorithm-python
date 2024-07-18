import sys
sys.setrecursionlimit(2500)

N, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0

def sol(index, current_sum):
    global count
    # 모든 인덱스를 돌았을때 종료 
    if index == N:
        return
    
    # current_sum에 현재 인덱스값 더해줌
    current_sum += nums[index]
    #S와 같은지 판별후 카운트+1
    if current_sum == S:
        count += 1
    # 결과값이 어떻든간에 방금수를 그대로 가져가면서 index를 늘리거나
    sol(index + 1, current_sum)
    # 방금수를 뺀 상태에서 index를 늘려줌
    sol(index + 1, current_sum - nums[index])

sol(0, 0)
print(count)
