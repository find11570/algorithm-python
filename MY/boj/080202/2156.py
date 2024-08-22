n = int(input())
wine = [int(input()) for _ in range(n)]
d = [0]*n

# 현재 포도주를 마실 지 말지를 결정 할 때는
# ① 현재 포도주와 이전 포도주를 마시고 전전 포두주는 마시지 않는다. ( wine[i]+wine[i-1]+d[i-3])
# ② 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는다. ( wine[i]+d[i-2] )
# ③ 현재 포도주를 마시지 않는다. (d[i-1])
#d[n]= n잔까지 왔을때 최대값 .

d[0] = wine[0]
if n > 1:
    d[1] = wine[0]+wine[1]

if n > 2:
    d[2] = max(wine[2]+wine[1], wine[2]+wine[0], wine[0]+wine[1]) #0~2번까지 마셨을때 최대값

for i in range(3, n):
    d[i] = max(d[i-1], d[i-3]+wine[i-1]+wine[i], d[i-2]+wine[i])
    # d3 = max(d2,d0+wine2+wine3, d1 +wine3)
print(d[n-1])                                                   