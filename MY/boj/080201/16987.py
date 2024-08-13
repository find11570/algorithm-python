def sol(egg_inhand):
    global max_broken
    if egg_inhand == N: #가장 오른쪽 계란을 들었다면
        broken_count=sum(1 for dur,_ in eggs if dur<=0) #깨진 계란 수만큼 1더해줌
        max_broken=max(max_broken,broken_count)
        return
    #for egg in eggs:
    #   durability = egg[0]
    #   if durability <= 0:
    #       broken_count += 1

    if eggs[egg_inhand][0]<=0: #손에 든 계란이 깨져있음.
        sol(egg_inhand+1) #다음계란 손에 쥠
        return
    
    #손에든 계란이 깨지지 않음.
    hit=False #깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다. 
    
    for i in range(N): #깨지지 않은 다른 계란이 있음.
        if i!=egg_inhand and eggs[i][0]>0: #지금 계란 스킵 및 이미 타겟계란이 깨졌는지 체크
            hit=True # 때릴 계란 발견
            eggs[egg_inhand][0]-=eggs[i][1]
            eggs[i][0]-=eggs[egg_inhand][1]
            sol(egg_inhand +1)
            #다음 recursion을 위해 계란복구
            eggs[egg_inhand][0]+=eggs[i][1]
            eggs[i][0]+=eggs[egg_inhand][1]
    
    if not hit:#깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다. 
        sol(egg_inhand+1)

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
max_broken=0
sol(0) #손에 0번 계란부터 시작
print(max_broken)
