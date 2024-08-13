def solution(k, dungeons):
    visited=[False]*len(dungeons)
    def backtrack(energy,dungeons,visited,depth):
        max_try=depth
        for i in range(len(dungeons)):
            if energy>=dungeons[i][0] and visited[i]==False:
                visited[i]=True
                max_try=max(max_try,backtrack(energy-dungeons[i][1],dungeons,visited,depth+1))
                visited[i]=False
        return max_try
    answer = backtrack(k,dungeons,visited,0)
    return answer