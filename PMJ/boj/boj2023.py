import sys
sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())
def isPrime(a):
    for i in range(2,a//2+1):
        if(a%i==0):
            return False
    return True

def dfs(number,j):
    if(j==N):
        if(isPrime(number)):
            print(number)
    else:
        for i in range(1,10,2):
            if(isPrime(number*10+i)):
                dfs(number*10+i,j+1)

dfs(2,1)
dfs(3,1)
dfs(5,1)
dfs(7,1)
