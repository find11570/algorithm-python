N = int(input())
row = [0]*N  # 행과 열중 하나만 같아도 해당하므로 하나만 써줘도 된다.
cnt = 0
# 퀸 공격조건 1 y2=y1, x2=x1, y2-y1=x2-x1(대각선) (행과 열끼리의 차이가 같을때)

def promising(num):
    for i in range(num):            #행과 열의 차이가 같을때
        if row[num] == row[i] or abs(row[num]-row[i]) == abs(num-i):
            # 같은 행이나 열에 있거나 대각선에 존재하면
            return False
    return True

def sol(y): #다음 행에서 퀸 갯수 추가하기
    global cnt
    if y == N:  # 마지막 행에 다다르면 종료
        cnt += 1 #경우의수 +1
        return
    else:
        for x in range(N): #N==4
            row[y] = x # (y,x)에 퀸 놓기
            if promising(y):# 그자리가 가능하면
                sol(y+1) # 다음 행으로


sol(0)
print(cnt)
