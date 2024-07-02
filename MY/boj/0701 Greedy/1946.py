import sys
input=sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    #지원자 성적 A,B성적순 나열 
    scores = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))

    cnt = 0
    A = B = N #지원자 최저등수
    for a, b in scores:
        if A > a or B > b: #바교할 지원자가 최저등수보다 한개라도 높으면
            A = a #해당지원자의 성적을 비교군으로 바꿔줌.
            B = b
            cnt += 1
    print(cnt)
