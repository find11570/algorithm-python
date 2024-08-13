from collections import deque
def solution(s):
    s=deque(s)
    answer=0
    for i in range(len(s)):
        if i!=0:
            s.rotate(-1)            
        stk=[]
        for j in s: #왼쪽일때
            if j=="[" or j=="(" or j=="{":
                stk.append(j)
            else: #오른쪽일때
                if not stk: #스택 비었음
                    break
                last=stk.pop()
                if last=="[" and j!="]":
                    break
                elif last=="(" and j!=")":
                    break
                elif last=="{" and j!="}":
                    break
        else:
            if not stk:
                answer+=1                    
                    
    return answer