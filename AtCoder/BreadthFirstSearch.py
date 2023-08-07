import copy
from collections import deque

n,x,y=map(int, input().split())
g=[[] for _ in range(n)]
Q=deque()
seen=[False]*n #探索済チェック用
dist=[0]*n #距離計測用
previous =[0]*n #探索経路用

#入力の受け取り
for i in range(n-1):
    u,v=map(int,input().split())
    u=u-1
    v=v-1
    g[u].append(v)
    g[v].append(u)

Q.append(0)#始点をキューに追加
previous[0] = -2 #始点には-2
while(len(Q)) > 0:
    vertex = Q.popleft() #先入れ先出し
    #vertex = Q.pop #後入れ先出し
    seen[vertex] = True

    for next in g[vertex]:
        if seen[next]: continue #探索済みはスルー
            
        dist[next] = dist[vertex] + 1 #距離を格納

        #探索経路を1つ前の頂点を追加
        previous[next] = vertex

        Q.append(next)#キューに次を追加

ans = []
now = 5 #頂点5から始点までの最短経路復元
ans.append(now)
while previous[now] != -2:
    now = previous[now]
    ans.append(now + 1)

print(*ans[::-1])