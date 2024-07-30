import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())

# 초기값 설정
lst = [1, 3]

# 동적 계획법을 사용한 방법의 수 계산
for i in range(2, n):
    lst.append(lst[i-1] + 2 * lst[i-2])
    # d[n]= d[n-1]+d[n-2]*2
# 결과 출력
print(lst[-1] % 10007)


# 그림참고
# https://semperparatus.tistory.com/108
