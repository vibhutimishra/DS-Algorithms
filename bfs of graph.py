def bfs(g,N):
    queue=[]
    visited=[]
    ans=[]
    for i in range(N):
        visited.append(0)
    queue.append(0)
    while len(queue)!=0:
        l=len(g[queue[0]])
        if visited[queue[0]]==0:
            visited[queue[0]]=1
        for i in range(l):
            if visited[g[queue[0]][i]]==0:
                visited[g[queue[0]][i]]=1
                queue.append(g[queue[0]][i])
        ans.append(queue[0])
        queue.pop(0)

    return ans
