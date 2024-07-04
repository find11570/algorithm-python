# 신입 사원 # 1946
import sys

t = int(sys.stdin.readline())
result = []
for _ in range(t) :
    n = int(sys.stdin.readline())
    rank = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    rank.sort()

    count = 1
    top = rank[0][1] # 최고값만 교체하면서 비교
    for i in range(1, n) :
        if rank[i][1] < top :
            count += 1
            top = rank[i][1]
    result.append(count)

for i in result :
    print(i)