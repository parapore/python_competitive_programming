import sys
sys.setrecursionlimit(10**6)

N=int(input())
T=[list(map(int,input().split())) for _ in range(N)]
seen=[False]*N

time=0
def dfs(v):
  seen[v-1] = True
  global time
  count = 0
  for next in T[v-1]:
    count+=1
    if count == 1:
      time+=next
      continue
    if count == 2 or seen[next-1]:
      continue
    dfs(next)

dfs(N)
print(time)