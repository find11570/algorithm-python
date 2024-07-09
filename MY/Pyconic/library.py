
from queue import PriorityQueue
import math
from math import sqrt
from math import pi, e
from math import factorial

from bisect import bisect_left, bisect_right

from itertools import combinations_with_replacement
from itertools import product
from itertools import combinations
from itertools import permutations

from collections import Counter
from collections import deque


# Counter
# from collections import Counter
# 등장횟수를 세는 기능
# iterable object 가 주어졌을때 내부의 element 가 몇번 등장했는지 알려줌
counter = Counter(['red', 'blue', 'red', 'blue', 'green', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))  # 사전 자료형으로 변환
print()

# 순열
# from itertools import permutations
# 서로다른 n개에서 서로다른 r개를 선택하여 일렬로 나열
data = ['a', 'b', 'c']
result = list(permutations(data, 3))
print(result)

print()
# 중복순열 from itertools import product
result = list(product(data, repeat=2))  # 2개를 뽑는 순열(중복허용)
print(result)
print()

# 조합
# from itertools import combinations
# 서로다른 n개에서 순서를 고려하지않고 서로다른 r개를 뽑음
data = ['a', 'b', 'c']
result = list(combinations(data, 3))
print(result)
print()

# 중복조합
# from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))  # 2개를 뽑는 모든 조합(중복허용)
print(result)
print()

# 최대 공약수와 최소 공배수
# import math


def lcm(a, b):
    return a*b//math.gcd(a, b)


a = 21
b = 14

print(math.gcd(21, 14))  # 최대 공약수 GCD계산
print(lcm(21, 14))  # 최소 공배수 lcm 계산


# 이진탐색 을 쉽게 구현
# from bisect import bisect_left, bisect_right
# #정렬되어있는 배열에서 특정한 원소를 찾아야 할때 매우 효과적
# bisect_left(a,x):정렬된 a에 x를 삽입할 위치를 리턴, x가 a에 이미 있으면 기존 항목의 앞 (왼쪽)의 위치를 반환
# bisect_right(a,x):정렬된 a에 x를 삽입할 위치를 리턴, x가 a에 이미 있으면 기존 항목 뒤 (오른쪽)의 위치를 반환
data = [1, 4, 5, 2, 2, 3, 19, 192, 39]
data.sort()  # 정렬 필수
# [1, 2, 2, 3, 4, 5, 19, 39, 192]
target = 2
print(bisect_right(data, 2))
print(bisect_left(data, 2))

A = [1, 1, 2, 3, 5, 7, 8]
# 인덱스 6

print(bisect_left(A, 5))  # 4
print(bisect_right(A, 5))  # 5

# 응용 : 특정 범위에 속하는 원소의 개수 구하기


def countsByRange(nums, left, right):
    right_range = bisect_right(nums, right)
    left_range = bisect_left(nums, left)
    return right_range-left_range


print(countsByRange(A, 2, 9))  # 4

# deque : 데이터의 시작이나 끝에 삽입,삭제할때 효과적
# from collections import deque
# popleft()첫번째 원소제거
# pop() 마지막 원소제거
# appendleft(x): 첫번째 인덱스에 x 삽입
# append(x) : 마지막 인덱스에 x 삽입
# lotate(k)  # 오른쪽으로 k만큼 원소들을 이동
data = deque([2, 3, 4])
print(data)
data.append("append")
print(data)
data.appendleft("append")
print(data)
data.pop()
print(data)
data.popleft()
print(data)
data.rotate(1)  # 오른쪽으로 k만큼 원소들을 이동
print(data)
data.rotate(-1)  # 왼쪽으로 k만큼 원소들을 이동
print(data)

# 우선순위 큐
# from queue import PriorityQueue
que = PriorityQueue()
que.put(4)
que.put(10)
que.put(2)
for i in range(len(que.queue)):
    print(que.queue[i], end=" ")
print()
que.get()  # 우선순위 큐 제거 (2)
print(que)
print(que.queue[1])
# 팩토리얼
# from math import factorial
print(factorial(3))

# 제곱근
# from math import sqrt
print(sqrt(4))

# pi,e
# from math import pi,e
print(pi)
print(e)
