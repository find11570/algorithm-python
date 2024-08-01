def recur(num):
    if len(ans) == M:
        return print(*ans)
    for i in nums:
        #해당 숫자가 배열에 있지 않을경우 추가
        if i not in ans:
            ans.append(i)
            recur(i+1)
            #다시 뺴줘야함 
            ans.pop()
#6603 문제는 뒤의 숫자가 먼저 올수가 없기 떄문에 차이가 있다.

N,M=map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []
recur(0)
