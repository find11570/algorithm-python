# A -> B # 16953
# a -> b로 만들지, b -> a 로 만들지 고민
import sys

a, b = map(int, sys.stdin.readline().split())
cnt = 1
# b -> a로 만들기
while a != b :
    if b % 10 == 1 : # 끝 자리가 1 일때
        b = int(b / 10) # 1 떼기
        cnt += 1
    elif b % 2 == 0 and b != 0 : # b != 0 조건 없으면 무한 루프
        b = int(b / 2)
        cnt += 1
    else :
        cnt = -1
        break

print(cnt)