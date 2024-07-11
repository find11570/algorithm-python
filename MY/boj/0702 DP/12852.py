#dp[i] : i를 1로 만들 수있는 최소한의 방법에 포함되어 있는 수들로 이루어진 리스트
#dp를 빈 배열로 잡고 방법의 최소값이 갱신될때마다 dp[i]의 값을 수정해준다.
N=int(input())
dp=[[] for _ in range(N+1)]
dp[1]+=[1] # 1이 1이 될수있는 경우.

for i in range(2,N+1): #2부터 N까지 1로 만들 수있는
    dp[i]=dp[i-1]+[i]
    #dp[2]= dp[1] + [2]
    #dp[2]= [1,2]

    #dp[3]=[1,2,3]
    if i%3==0:
        #dp[1]+1<len(dp[3])
        #dp[1]+1<3
        # dp[3]=dp[1]+[3]
        # dp[3]=[1,3] 
        if len(dp[i//3])+1<len(dp[i]):
            dp[i]=dp[i//3]+[i]
    
    if i%2==0:
        if len(dp[i//2])+1<len(dp[i]):
            dp[i]=dp[i//2]+[i]

#본래 수가 포함된 길이 이므로 1을 빼줌
print(len(dp[N])-1)
#각 dp 는 1부터 N 까지의 경로를 담고 있으므로 역으로 출력
print(*dp[N][::-1])