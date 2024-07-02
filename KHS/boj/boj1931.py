# 회의실 배정 # 1931
import sys

meeting = int(sys.stdin.readline())
meeting_list = []
count = 0
cur = 0

for _ in range(meeting) :
    start, end = map(int, sys.stdin.readline().split())
    meeting_list.append([start, end])

# 종료 시간을 기준으로 정렬, 만약 종료 시간이 같다면 시작 시간을 기준으로 정렬
meeting_list.sort(key=lambda x: (x[1], x[0])) 

for i, _ in enumerate(meeting_list) :
    if cur <= meeting_list[i][0] :
        count += 1
        cur = meeting_list[i][1]

print(count)