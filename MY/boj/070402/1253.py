import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
num.sort()  # 숫자 정렬
cnt = 0

for i in range(n):
    goal = num[i]  # 목표숫자 해당 인덱스값
    i_index = 0  # 맨처음부터 목표숫자 바로 이전 인덱스 end로 설정
    j_index = n-1
    while i_index < j_index:  # 시작 인덱스가 끝 인덱스 이전 이 될때까지
        sum = num[i_index] + num[j_index]

        if sum < goal:  # 숫자가 적으면  시작인덱스 +1
            i_index += 1
        elif sum > goal:  # 숫자가 크면 끝인덱스 -1
            j_index -= 1

        else:  # 목표숫자와 같을 경우에
            if i_index != i and j_index != i:  # 목표숫자 인덱스와 다르다면 count+1
                cnt += 1
                break
            if i_index == i:    # 시작인덱스나 끝인덱스가 목표인덱스와 같다면 각각 1을 더하거나 빼줌
                i_index += 1
            elif j_index == i:
                j_index -= 1
print(cnt)
