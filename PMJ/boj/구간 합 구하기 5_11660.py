import sys
input = sys.stdin.readline

size, times = map(int, input().split()) // 2차원 배열의 크기 size, 구간합을 구해야하는 좌표들을 받을 횟수 times
arr = [list(map(int, input().split())) for i in range(size)] // size만큼 반복하며 list로 입력을 받는다
sum = [[0 for j in range(size+1)] for i in range(size+1)] // 누적합을 저장할 배열 생성. 구간합의 좌표가 0부터가 아닌 1부터 시작이므로 좌표값을 맞춰주기 위해 0번 index생성
for i in range(1, size+1):
    for j in range(1, size+1):
        sum[i][j] = sum[i-1][j] + sum[i][j-1] + arr[i-1][j-1] - sum[i-1][j-1] // 누적합 배열 입력 기본 배열인 arr은 0번 index부터 사용하므로 1로 시작하는 누적합 배열에 더할 때 index값을 1씩 뺴줌

// 구간합의 공식은 누적합[x2][y2] - 누적합[x2][y1-1] - 누적합[x1-1][y2] + 누적합[x1-1][y1-1]이므로 구간합을 구해야하는 횟수(times)만큼 반복하며 출력한다
for i in range(times):
    x1,y1,x2,y2 = map(int, input().split())
    print(sum[x2][y2] - sum[x2][y1-1] - sum[x1-1][y2] + sum[x1-1][y1-1])
    
