
# https://www.acmicpc.net/problem/20300
import sys
sys.stdin = open("input.txt","r")

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = []

if(len(arr)%2==1):
    result.append(arr[-1])
    arr = arr[:-1]
for i in range(len(arr)//2):
    result.append(arr[i] + arr[len(arr)-1-i])

print(max(result))