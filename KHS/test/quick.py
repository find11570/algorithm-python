def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    print("pivot : " , pivot, " => ", end="")
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(left, middle, right)
    print("sort", quickSort(left), middle, quickSort(right))
    return quickSort(left) + middle + quickSort(right)

# 예시 배열
arr = [38, 18, 8, 25, 51, 33]
# arr = [ 6, 2, 4, 3, 5 ]
print("원본 배열:", arr)
sorted_arr = quickSort(arr)

print("정렬된 배열:", sorted_arr)