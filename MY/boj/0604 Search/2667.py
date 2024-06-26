import sys
input=sys.stdin.readline
N=int(input())
map=[list(map(int,input().strip())) for _ in range(N)]
chk=[[False]*N for _ in range(N)]
ans=[]
dy=[-1,1,0,0]
dx=[0,0,-1,1]

def dfs(y,x):
    global size
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<N and 0<=nx<N:
            if chk[ny][nx]==False and map[ny][nx]==1:
                size+=1 #방문하지 않았고 단지번호존재
                chk[ny][nx]=1
                dfs(ny,nx) #dfs 재귀 이용

for i in range(N):
    for j in range(N):
        if chk[i][j]==False and map[i][j]==1:
            size=1 # dfs 들어가기전 size 리셋
            chk[i][j]=True
            dfs(i,j) 
            ans.append(size) #첫 dfs 에서 여러번의 dfs 가 돌아간뒤 첫 size가 들어가게됨

print(len(ans))
for i in sorted(ans):#정렬출력 
    print(i)