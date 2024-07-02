N = int(input().strip())

five = N // 5

while five >= 0:
    remainding = N - five * 5
    if remainding % 2 == 0:
        two = remainding // 2
        print(two + five)
        N = 0
        five = -1
    five -= 1

if (N != 0):
    print(-1)