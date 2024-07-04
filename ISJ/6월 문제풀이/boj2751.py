import sys
import random

def quick_sort(arr):
    def sort(low, high):
        while low < high:
            if high - low < 10:
                insertion_sort(arr, low, high)
                return
            pivot_index = partition(low, high)
            # Recursively sort the smaller partition to limit stack depth
            if pivot_index - low < high - pivot_index:
                sort(low, pivot_index - 1)
                low = pivot_index + 1
            else:
                sort(pivot_index + 1, high)
                high = pivot_index - 1
    
    def partition(low, high):
        # Randomized pivot selection
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = arr[high]
        
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i
    
    def insertion_sort(arr, low, high):
        for i in range(low + 1, high + 1):
            key = arr[i]
            j = i - 1
            while j >= low and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    
    sort(0, len(arr) - 1)
    return arr

# Reading input from stdin
input_data = sys.stdin.read().split()
N = int(input_data[0])
array = list(map(int, input_data[1:N+1]))

# Sorting the array using optimized quicksort
sorted_array = quick_sort(array)

# Printing each element of the sorted array on a new line
for elem in sorted_array:
    print(elem)