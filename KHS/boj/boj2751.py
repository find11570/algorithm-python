# 수 정렬하기 2 # 2751
import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n) : # 입력
    num = int(sys.stdin.readline())
    arr.append(num)

# arr.sort()

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # 병합 과정: L과 R을 병합하여 arr에 저장
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # L에 남아 있는 요소들을 arr에 복사
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # R에 남아 있는 요소들을 arr에 복사
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

sorted_arr = merge_sort(arr)

for i in sorted_arr : # 출력
    print(i)