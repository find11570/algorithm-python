def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        flag = True
        for j in range(i + 1, len(prices)):
            if (prices[i] > prices[j]):
                answer.append(j - i)
                flag = False
                break;
            else:
                count += 1
        if (flag):
            answer.append(count)

    return answer

print(solution([1, 2, 3, 2, 3]))