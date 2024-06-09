import sys
total_numbers = int(input())
number_list = list(map(int, sys.stdin.readline().split()))
number_list.sort()
answer = 0
    
for i in range(total_numbers):  
    target = number_list[i]
    low, hi = 0 , total_numbers - 1
    while low < hi:
        if low == i:
            low += 1
            continue
        if hi == i:
            hi -= 1
            continue
        
        summ = number_list[low] + number_list[hi]
        if summ == target:
            answer += 1
            break
        elif summ < target:
            low += 1
        else:
            hi -= 1

print(answer)