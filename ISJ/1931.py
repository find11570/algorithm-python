n=int(input())
time=[]
for i in range(n):
    start,end=map(int,input().split())
    time.append([start,end])
time = sorted(time, key=lambda x: (x[1], x[0]))
count=1
end_time=time[0][1]
for i in range(1,n):
    if time[i][0]>=end_time:
        count+=1
        end_time=time[i][1]
print(count)