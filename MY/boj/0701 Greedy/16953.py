import sys
input = sys.stdin.readline
# A와 B 입력
a, b = map(int, input().split())
count = 1  # 변환 횟수 필요한 연산의 최솟값에 1을 더한 값이므로 카운트는 1부터 시작

while (a < b):  # A가 B보다 작은동안
    if (b % 2 == 0):  # B가 2로 나눠진다면, B를 2로 나누고
        b = b // 2 
    else:   # 나눠지지 않는다면,
        if (int(str(b)[-1]) == 1):  #B의 가장 오른쪽이 1이라면 가장 오른쪽에서 1을 제거한다.
            b = int(str(b)[:-1])  
        else:   # B의 가장 오른쪽이 1이 아니라면 변환 불가능
            break
    count += 1  # 변환 횟수 증가

if (a == b):  # A와 B가 같다면
    print(count)
else:  # 변환 불가능하다면
    print(-1)
