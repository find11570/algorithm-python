def recur(num):
    if len(ans) == 6:
        return print(*ans)
    for i in range(num, N):
        ans.append(nums[i])
        recur(i+1)
        ans.pop()


while True:
    N, *nums = map(int, input().split())
    if N == 0:
        exit()
    ans = []
    recur(0)
    print()
