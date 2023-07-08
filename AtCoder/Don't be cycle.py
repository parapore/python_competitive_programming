import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
seen = [False]*n

def dfs(num):
    seen[num] = True
    for next in g[num]:
        if seen[next]:
            continue
        dfs(next)

for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

#連結成分の個数を数える
renketu = 0
for i in range(n):
    if not seen[i]:
        renketu +=1
        dfs(i)

# 連結成分の数が1個とは限らないので、連結成分の数を数える
# 閉路なしの連結成分の辺の数は頂点数-1
# 答えは 辺の数ー（頂点数ー1ー連結成分の個数＋１）
print(m-(n-renketu))