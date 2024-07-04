#https://school.programmers.co.kr/learn/courses/30/lessons/120880
#https://school.programmers.co.kr/learn/courses/30/lessons/120866?language=python3

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    index = 2
    array = []
    
    for i in range(N):
        array.append([int(data[index + j]) for j in range(N)])
        index += N
    
    prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix_sum[i][j] = array[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
    
    results = []
    for _ in range(M):
        x1 = int(data[index])
        y1 = int(data[index + 1])
        x2 = int(data[index + 2])
        y2 = int(data[index + 3])
        index += 4
        
        result = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]
        results.append(result)
    
    for res in results:
        print(res)
if __name__ == "__main__":
    main()