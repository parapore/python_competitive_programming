import copy
from collections import deque
from collections import defaultdict

n = int(input())
g = [[] for _ in range(n)]
Q=deque()
seen=[False]*n #探索済チェック用
dist=[0]*n #距離計測用
route = defaultdict(list) #探索経路用

#入力の受け取り
for i in range(n-1):
    u,v=map(int,input().split())
    u=u-1
    v=v-1
    g[u].append(v)

Q.append(0)#始点をキューに追加
route[0] = [0]#始点を探索経路に追加
while(len(Q)) > 0:
    vertex = Q.popleft() #先入れ先出し
    #vertex = Q.pop #後入れ先出し
    for next in g[vertex]:
        if seen[next]: #探索済みはスルー
            continue

        dist[next] = dist[vertex] + 1 #距離を格納

        #探索経路を追加
        parentRoute = copy.copy(route[vertex])
        parentRoute.append(next)
        route[next] = parentRoute

        Q.append(next)#キューに次を追加
    