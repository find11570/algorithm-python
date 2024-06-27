
import sys
sys.stdin = open("input.txt","r")

N = int(input())
arr = []
for _ in range(N):
    i = int(input())
    arr.append(i)

arr.sort()
for i in arr:
    print(i)