import sys
sys.stdin = open("input.txt","r")

N= int(input())
arr =[list(map(int,input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1],x[0]))

end = 0
ans = 0

for x,y in arr:
    if(x>=end):
        ans += 1
        end = y
    else:
        continue
print(ans)