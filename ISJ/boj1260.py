from collections import deque

def is_prime(num):
    if (num < 2):
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
            
def DFS(N):
    queue = deque([2,3,5,7])
    while queue:
        current = queue.popleft()
        if N == len(str(current)):
            print(current)
        
        else :
            for i in range (1,10):
                value = current * 10 + i
                if (is_prime(value)):
                    queue.append(value)

N = int(input())
DFS(N)
