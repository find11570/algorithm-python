# https://www.acmicpc.net/problem/1541

import sys
sys.stdin = open("input.txt","r")
str = input().split("-")
arr = []

for i in str:
    a = list(map(int,i.split("+")))
    arr.append(sum(a))

sum = arr[0]

for i in range(1,len(arr)):
    sum -= arr[i]

print(sum)
