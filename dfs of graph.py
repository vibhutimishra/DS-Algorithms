def dfsFinal(g,visited,i,ans):
    if visited[i]==0:
        visited[i]=1
        ans.append(i)
        l=len(g[i])
        if l==0:
            return
        for j in range(l):
            dfsFinal(g,visited,g[i][j],ans)
    return ans

def dfs(g,N):
    visited=[]
    ans=[]
    for i in range(N):
        visited.append(0)
    ans=dfsFinal(g,visited,0,ans)
    return ans
