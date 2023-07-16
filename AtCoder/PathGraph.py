
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
seen = [False]*n

def dfs(v):
    seen[v] = True
    if len(g[v]) > 2:#3辺以上持つ頂点があったらNo
        print("No")
        exit()
    
    for next in g[v]:
        if seen[next]:
            continue
        dfs(next)


for i in range(m):
    v1,v2 = map(int, input().split())
    g[v1-1].append(v2-1)
    g[v2-1].append(v1-1)

# 辺が1この頂点探す(スタート地点)
start = -1
for i in range(n):
    if len(g[i]) == 1:
        start = i
if start == -1:#1個もなければNo
    print("No")
    exit()

dfs(start)

if all(seen):#全探索済みならYes
    print("Yes")
else:
    print("No")

