def dfsFinal(g,visited,i,ans,rec,N):
    rec[i]=1
    visited[i]=1
    l=len(g[i])
    if l==0:
        rec[i]=0
        return 0
    for j in range(l):
        if g[i][j] == i:
            return 1
        if visited[g[i][j]]==0:
            ans = dfsFinal(g,visited,g[i][j],ans,rec,N)
        elif rec[g[i][j]] == 1:
            return 1
        if ans==1:
            return 1
    rec[i]=0
    return 0


def isCyclic(N, g):
    visited=[]
    ans=[]
    recursion=[]
    for i in range(N):
        visited.append(0)
        recursion.append(0)
    for i in range(N):
        if visited[i]==0:
            ans=dfsFinal(g,visited,i,ans,recursion,N)
        if ans==1:
            return 1
    return ans
