import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
g = [[] for _ in range(n)]
seen = [False]*n

for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

def dfs(num):
    seen[num] = True
    for to in g[num]:
        if seen[to]:
            continue        
        dfs(to)

dfs(0)

if sum(seen) == n:
    print("The graph is connected.")
else:
    print("The graph is not connected.")