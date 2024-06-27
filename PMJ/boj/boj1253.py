
import sys

sys.stdin = open("input.txt","r")

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0
for i in range(n):
    start = 0
    end = len(arr)-1
    while start < end:
        if arr[start] + arr[end] == arr[i]:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                count += 1
                break
        elif arr[start] + arr[end] > arr[i]:
            end -= 1
        elif arr[start] + arr[end] < arr[i]:
            start += 1

print(count)









