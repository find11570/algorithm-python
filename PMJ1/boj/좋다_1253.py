import sys
input = sys.stdin.readline

N = int(input()) # 수의 개수 입력받기
nums = list(map(int, input().split())) # N개의 수 배열 저장
nums.sort() # 배열 오름차순 정렬
count = 0 # 좋은 수를 세는 변수
for i in range(0, N):
    target = nums[i] # 좋은수인지 알아봐야할 수
    start = 0 # 투 포인터의 시작 초기화
    end = N - 1 # 투 포인터의 끝 초기화
    while start < end : # 시작이 끝보다 작은 동안만 돌아야함
        sum = nums[start] + nums[end]
        if target == sum: # 좋은수인지 검증하는 수와 포인터의 합이 맞다면?
            if i == start: # 자신은 답이 될 수 없으므로 start는 1증가
                start += 1
            elif i == end: # 자신은 답이 될 수 없으므로 end는 1감소
                end -= 1
            else: # 위의 두경우가 아닌 경우 좋은수 !
                count += 1
                break
        elif sum > target : # 오름차순으로 정렬했으므로 투포인터의 합이 검증해야하는 수 보다 크다면 end가 왼쪽으로 가서 합이 감소되어야함
            end -= 1
        else : # 만일 투포인터의 합이 검증해야하는 수보다 작다면 합이 커져야 하므로 start가 증가해야함
            start +=1
print(count)
