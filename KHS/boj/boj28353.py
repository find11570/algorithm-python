# 고양이 카페 # 28353
n, k = map(int, input().split()) # n = 고양이 수, k = 최대 무게
cat_weight = list(map(int, input().split()))
cat_weight.sort()

start, end = 0, n - 1

result = 0

while start < end:
    if cat_weight[start] + cat_weight[end] <= k:
        start += 1
        end -= 1
        result += 1
    else:
        end -= 1
    
print(result)