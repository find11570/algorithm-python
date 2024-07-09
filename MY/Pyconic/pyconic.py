#1.정수와 배열이 같은 줄에 들어오는경우
#4 / 10 20 30 40
N,*arr=map(int,input().split())

#2. 문자열을 한 글자씩 배열에 저장
#arr = [['A', 'A', 'A', 'A']
#    ['A', 'B', 'C', 'A']
#    ['A', 'A', 'A', 'A']]
arr = [list(input()) for _ in range(N)]

#3.배열 연결해서 출력
#arr=[1,2,3,4]
print("".join(map(str, arr))) #1234
#map 을이용해 string 으로 변경 

print(*arr) #1 2 3 4

#4.정수 최대최소
import sys
ans=sys.maxsize # 최대값 출력

#5.진법 10-> 2 8 16진수
bin(42) #2 
# >'0b101010' 
oct(42) #8
# >'0o52' 
hex(42) #16
# >'0x2a'

#6. 2 8 6진수->10진수
int('0b111100', 2) 
# 60
int('0o74', 8) 
# 60
int('0x3c', 16)
# 60

print(int(A,2)+int(B,2)) #2진수 덧셈

#7. 문자열 거꾸로
alph = "ABCD"
alph[::-1]

#8.배열 원소거꾸로
arr.reverse()

#배열정렬
arr.sort(key=lambda x:(x[0], x[1]))
# x[0] (x좌표)을 정렬하고, x[0] 값이 같다면 x[1] (y좌표)을 기준으로 오름차순 정렬

res = a if a > b else b


# round(number [, ndigits ])
# number -> 수 혹은 수를 담은 변수
# ndigits -> 몇 번째 자리수까지 표현할 것인지 지정. 첫 번째 자리로 지정하면 두 번째 자리에서 반올림을 수행한다
round(20/3)		# 7
round(20/3, 0)		# 7.0
round(20/3, 1) 		# 6.7
round(20/3, 2)		# 6.67
round(20/3, 3)		# 6.667
round(20/3, 4) 		# 6.6667

#전치행렬 (외우지 않아도됨..for i j 거꾸로 하면 되니까)
graph = [list(map(int, input().split())) for _ in range(N)]
graph2 = list(map(list, zip(*graph)))

#리스트 안에 리스트
list1 = [1, [2, [3, [4], 5], 6], 7]
ans = []
def recur(array):
    # Check if the current element is a list by attempting to iterate over it
    for element in array:
        if isinstance(element, list):  # Remove any isinstance calls and find a workaround
        #if type(element)==list:
            recur(element)
        else:
            ans.append(element)
recur(list1)
print(ans)