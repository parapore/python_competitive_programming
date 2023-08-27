import heapq
from collections import defaultdict

q=int(input())
S=defaultdict(int)
small=[]
large=[]

maxS=0
minS=10**9+1
for i in range(q):
  qtp = tuple(map(int, input().split()))
  if qtp[0] == 1:
    x = qtp[1]
    heapq.heappush(small, x)
    heapq.heappush(large, -x)
    S[x]+=1
  elif qtp[0]  == 2:
    x=qtp[1]
    c=qtp[2]
    S[x] -= min(c, S[x])


  else:
    minS = small[0]
    largeS = -large[0]
    while S[minS] == 0:#最小値が存在しないならプライオリティキューから削除する
      heapq.heappop(small)
      minS = small[0]
    
    while S[largeS] == 0:#最大値が存在しないならプライオリティキューから削除する
      heapq.heappop(large)
      largeS = -large[0]

    print(-large[0] - small[0])