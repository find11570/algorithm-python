str = input()
flag = True

str = str.split('-')
answer = 0
for idx, val in enumerate(str):
    if len(val.split("+")) == 1:
        num = int(val)
    else:
        num = sum(map(int, val.split("+")))

    if idx == 0:
        answer += num
    else:
        answer -= num
print(answer)