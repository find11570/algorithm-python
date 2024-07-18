N,M=map(int,input().split())
ans=[]
chk=[False]*(N+1)
def sol(count):
    global ans
    if count==M: # Count 가 뽑으려는 개수와 같다면 
        print(*ans) #출력후 함수 종료
        return
    for i in range(1,N+1):
        if chk[i]==False:
            chk[i]=True
            ans.append(i) #1은 방문체크 및 리스트에 넣어준상태에서
            sol(count+1) # count 1로 다시 함수 호출(재귀)
            chk[i]=False # [1]로 시작하는 경우들이 모두 끝나면 1의 방문체크를 해제해줌
            ans.pop() # [1] 제거 
    
sol(0)