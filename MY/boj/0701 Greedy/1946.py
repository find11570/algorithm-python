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
###################
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    # 입력
    N = int(input())
    applicant=sorted([list(map(int,input().split())) for _ in range(N)])
    # 정렬(서류 기준 오름차순)
    applicant.sort()  # 서류 등수 순으로 오름차순 정렬
    cut_line = applicant[0][1]  # 서류 1등의 면접 등수, 서류 등수로 이길 수 없으니 면접점수만 비교

    cnt = 1  # 합격자 수
    for i in applicant:
        # 서류는 앞 사람보다 낮지만, 면접 등수는 높은 참가자는 합격
        if cut_line > i[1]:
            cnt += 1
            cut_line = i[1]  # 면접 등수 컷라인이 높아짐. 서류로는 앞선 합격자보다 무조건 낮음 상대
            # 면접 등수로 이겨야 하기때문에 컷라인이 바뀜.
    print(cnt)


