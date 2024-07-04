# 팔 # 1105

import sys

L, R = map(str, sys.stdin.readline().split())

if len(L) != len(R): # 자릿수가 다르면 무조건 범위 안에 8을 포함하지 않는 수 있음.
    print(0)
else:
    cnt = 0
    for i in range(len(L)):
        if L[i] == R[i] and L[i] !='8':
            continue
        if L[i] == '8' and R[i] =='8':
            cnt += 1
        else:
            break
    print(cnt)