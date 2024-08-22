# i~j 강의가 한 블루레이 강의순서 바뀌면 안됨
# 각 M개의 블루레이의 크기는 같음
# 블루레이 크기 최소여야함
# 각 블루레이의 강의가 크기가 작은건 많이 큰건 적게 퍼져야됨
M,M=map(int,input().split())
lectures=list(map(int,input().split()))
# left 강의 최소
# right 강의 최대
# 강의를 순서대로 블루레이에 넣고 길이는 mid
# 강의를 넣고 나온 블루레이의 개수가 M보다 크다면 left= mid+1
# 강의를 넣고 나온 블루레이의 개수가 M보다 작다면 right=mid+1,answer=mid
# 블루레이의 개수가 M보다 적으면 용량을 줄임
# 블루레이의 개수가 M보다 많으면 용량을 늘림
#  
ans=0
left,right=max(lectures),sum(lectures)
# 최소 9 ,최대 45
while left<=right:
    mid=(left+right)//2  #담을 블루레이 크기 
    total=0
    count=1
    for i in lectures:
        if total+i>mid:
            count+=1
            total=0
        total+=i
    if count<=M:
        ans=mid
        right=mid-1 #용량줄임
    else:
        left=mid+1 #용량 늘림 
print(ans)