import sys
sys.stdin = open("input.txt","r")

N,K = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
print(arr[K-1])