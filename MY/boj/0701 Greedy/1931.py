import sys
input = sys.stdin.readline
N = int(input())
# 끝나는 시간 순서대로 정렬, 같으면 시작시간도 고려해서 정렬
meetings = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
end = cnt = 0
for s, e in meetings:
    if end <= s: #이전회의의 끝나는 시간이 다음 회의 시작시간보다 작거나 같을 경우
        cnt += 1 #카운트 +1
        end = e #다음 회의 끝나는시간으로 end를 바꿔준다. 
print(cnt)
