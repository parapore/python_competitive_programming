from functools import cmp_to_key
from collections import defaultdict
from collections import deque

n,k=map(int, input().split())
c=list(map(int,input().split()))
que = deque()
candy=defaultdict(int)#色、数

for i in range(k):
    que.append(c[i])
    candy[c[i]]+=1
maxc = len(candy)

for i in range(k, n):
    color = que.popleft()
    candy[color]-=1
    if candy[color] == 0:
        del candy[color]
    que.append(c[i])
    candy[c[i]]+=1
    maxc = max(maxc, len(candy))

print(maxc)