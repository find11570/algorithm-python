members = [list(input()) for _ in range(5)]
print(members)
chk = [[False]*5 for _ in range(5)]
result=0

def dfs(y,x,cnt):
    #좌표,숫자
    global result
    if cnt>=4:
        return
    for i in range(x,25):

dfs(0,0,0)
