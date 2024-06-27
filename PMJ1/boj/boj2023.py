from collections import deque
import sys

def isPrime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True

def dfs(num, count, goal):
    if count == goal:
        print(num)
        return
    for i in range(1, 10):
        if i % 2 == 0:
            continue
        if isPrime(num * 10 + i):
            dfs(num * 10 + i, count + 1, goal)

N = int(input())

dfs(2, 1, N)
dfs(3, 1, N)
dfs(5, 1, N)
dfs(7, 1, N)