def solution(numbers, target):
    def backtrack(res,cnt):
        if cnt==len(numbers):
            answer.append(res)
            return    
        backtrack(res+numbers[cnt],cnt+1)
        backtrack(res-numbers[cnt],cnt+1)
    answer = []
    backtrack(0,0)
    return answer.count(target)