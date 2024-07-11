start, end = map(int, input().split())
cnt = 1
while end > start:
    if end % 10 == 1:
        trans = str(end)[:-1]
        end = int(trans)
    else:
        if not (end/2).is_integer():
            break
        else:
            end //= 2
    cnt += 1
print(cnt) if start == end else print(-1)
