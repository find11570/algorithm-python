import sys

N = int(input())
rooms = []
for _ in range(N):
    rooms.append(list(map(int, sys.stdin.readline().strip().split())))
rooms = sorted(rooms, key=lambda x: (x[1], x[0]))
start = rooms[0][0]
end = rooms[0][1]
cnt = 1
for i in range(1, N):
    if rooms[i][0] >= end:
        start = rooms[i][0]
        end = rooms[i][1]
        cnt += 1

print(cnt)
