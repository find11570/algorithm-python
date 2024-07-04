# 보석 도둑 # 1202
# 그리디로 풀려고 했는데 우선순위 큐로 해야 시간초과가 안남ㅠ
import sys

n, k = map(int, sys.stdin.readline().split())
jewel = [] # 보석 담을 공간
max = [] # 가방 무게
max_sum = 0 # 최대 무게
max_tmp = 0 # 가방의 담을 보석의 가격
max_idx = 0 # 가방의 담을 보석의 index. 담은 이후 pop하기 위해서.

for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    jewel.append([m, v])

for _ in range(k) :
    c = int(sys.stdin.readline())
    max.append(c)

jewel.sort(key=lambda x:(x[1], x[0]))
max.sort() # 작은 가방부터 차례대로 채우기

for i in max : 
    for idx, val in enumerate(jewel) :
        if i >= jewel[idx][0] :
            max_tmp = jewel[idx][1]
            max_idx = idx
            # print(i, " in ", jewel[idx][0])
            
    max_sum += max_tmp
    jewel.pop(max_idx)
    max_tmp = 0
    max_idx = 0

print(max_sum)