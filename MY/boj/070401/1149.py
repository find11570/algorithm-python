import sys
N = int(sys.stdin.readline())
RGB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N):
    # 현재 열을 제외한 i-1행의 열들 중 최솟값 + 현재 칸 비용
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2])+RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2])+RGB[i][1]
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1])+RGB[i][2]
print(min(RGB[N-1]))