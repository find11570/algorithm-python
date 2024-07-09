from heapq import nlargest
from heapq import nsmallest
from heapq import heapify
from heapq import heappush, heappop
import sys

heap = []  # heapq 에서 제공하는 함수 사용
heappush(heap, 4)  # heappush(list,element)
heappush(heap, 1)
heappush(heap, 7)
heappush(heap, 3)
heappush(heap, 8)
heappush(heap, 5)
print(heap)

# heap 에서 element 삭제
heappop(heap)  # heappop(제거할 리스트) ,가장 작은 원소 제거
print(heap)
heappop(heap)
print(heap)  # heap 규칙을 맞추기 위해 재배치
heappop(heap)
print(heap)
print()

print(heap[0])  # heap최소값 삭제하지 않고 접근 index 0만 접근가능
heappush(heap, 1)
print(heap[0])
print(heap)
print()

# heapify 기존리스트를 heap으로 변환
heap = [4, 1, 7, 3, 8, 5]
heapify(heap)
print(heap)
print()

# 원본 보존필요
nums = [4, 1, 7, 3, 8, 5]
heap = nums[:]  # list 복사
heapify(heap)
print(nums)
print(heap)
print()

# 최대 heap
nums = [4, 1, 7, 3, 8, 5]
heap = []
max_heap = []
for num in nums:
    heappush(heap, -num)  # 최소heap 의경우 heappush(heap,num)
#   heappussh(heap,(-num,num))
while heap:
    max_heap.append(-heappop(heap))
#   max_heap.append(heappop(heap)[1])
print(max_heap)

# 절대값 heap
ans = []
heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if not heap:
            ans.append(0)
        else:
            ans.append(heappop(heap)[1])
    else:
        heappush(heap, (abs(x), x))
while heap:
    ans.append(heappop(heap)[0])
print("절대값 힙", ans)

# n번째 최소값/최대값
# from heapq import nsmallest / from heapq import nlargest


def nth_smallest(nums, n):
    heap = []
    for num in nums:        # heap = nums[:]
        heappush(heap, num)     # heapify(heap)

    nth_min = None  # n번째로 작은값을 저장할 변수
    for _ in range(n):
        nth_min = heappop(heap)
    return nth_min


print()

print(nth_smallest([4, 1, 7, 3, 8, 5], 3))
print()

print(nsmallest(3, [4, 1, 7, 3, 8, 5]))  # nsmallest(n,list) 가장작은 n개의 리스트 반환
print(nsmallest(3, [4, 1, 7, 3, 8, 5])[-1])
print()

print(nlargest(3, [4, 1, 7, 3, 8, 5]))  # nlargest(n,list) 가장 큰n개의 list 반환
print(nlargest(3, [4, 1, 7, 3, 8, 5])[-1])
print()

# heap 정렬


def heap_sort(nums):  # heap_sort(list)
    heap = []
    for num in nums:
        heappush(heap, num)
    # print(heap)
    # heapify(nums)
    sorted_nums = []
    while heap:
        sorted_nums.append(heappop(heap))
    # for _ in range(len(heap)):
    #     sorted_nums.append(heappop(heap))
    return sorted_nums


print(heap_sort([4, 1, 7, 3, 8, 5]))
