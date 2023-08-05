from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

n = int(input())
g=defaultdict(set)
seen=defaultdict()

for i in range(n):
    a,b=map(int, input().split())
    a,b = a-1,b-1
    g[a].add(b)
    g[b].add(a)
    seen[a]= False
    seen[b] = False

ans=0
def dfs(v):
    seen[v]=True
    for next in g[v]:
        if seen[next]:
            continue
        global ans
        ans = max(ans, next)
        dfs(next)
        
    return ans
ans=max(dfs(0), ans)
print(ans+1)
