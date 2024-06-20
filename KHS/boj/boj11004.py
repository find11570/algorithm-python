# K번째 수 # 11004
import sys

n, k = map(int, sys.stdin.readline().split()) # n = 수의 개수, k = k번째 수 출력
array = list(map(int, sys.stdin.readline().split()))

# for i in range(len(array) - 1) :
#     if array[i] > array[i+1] :
#         array[i], array[i+1] = array[i+1], array[i]

# def quickSort(arr) :
#     if len(arr) <= 1 :
#         return arr
#     pivot = arr[len(arr) // 2]
#     # left = arr[:pivot] # 슬라이싱 == 중복값 처리 에러
#     # middle = [pivot]
#     # right = arr[pivot + 1:]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quickSort(left) + middle + quickSort(right)  

# sorted_arr = quickSort(array)
# print(sorted_arr[k-1])

array.sort()
print(array[k-1])