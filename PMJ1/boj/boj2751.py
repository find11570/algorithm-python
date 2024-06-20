import sys
def mergeSort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1
        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))

tc  =  int(sys.stdin.readline().strip())
arr = []
for _ in range(tc):
    arr.append(int(sys.stdin.readline().strip()))
mergeSort(arr)
for num in arr:
    print(num)
