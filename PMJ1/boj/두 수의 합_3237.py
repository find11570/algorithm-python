lenn = int(input()) // 수열의 크기를 입력받는 변수. 사용하지 않지만 입력값을 받아야하므로 지정함
nums = list(map(int, input().split())) // 수열을 입력받는 배열
arr = [0 for i in range(2000001)] // 입력받은 배열을 기억하기 위한 배열, 0으로 초기화해준다.
target = int(input()) // 합쳐서 나와야하는 숫자
count = 0

for num in nums:
    if target - num > 0 and arr[target - num] == 1:  
        count += 1
    arr[num] = 1 
// 합쳐서 나와야하는 숫자가 만약 3인데 입력받은 숫자가 1000이라면 index를 벗어나는 에러가 발생하므로 인덱스가 0을 넘는지에 대한 조건을 걸어줌
// 3을 구해야하는데 현재 나오는 숫자가 1이고 이전에 2(target-1)가 있는지 알기위해 index로 검색을 해서 그 값이 1이면 count를 1씩 늘려줌
// 이 숫자가 나온것을 기록하기 위해 해당 index에 1 값을 넣어줌. 이 조건이 무조건 숫자를 찾는 경우보다 뒤에 와야하는데 그이유는 target이 4고 현재나온수가 2이라면 맞다고 되므로 오답이됨
print(count)
