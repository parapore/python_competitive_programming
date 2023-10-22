import sys
sys.setrecursionlimit(10**6)

H,W=map(int,input().split())
S=[]
seen=[]
for i in range(H):
  S.append(list(input()))
  seen.append([False]*W)

dx=[1,1,1,0,0,-1,-1,-1]
dy=[0,1,-1,1,-1,0,1,-1]

def dfs(sh,sw):
  seen[sh][sw]=True
  for i in range(8):
    x=sw+dx[i]
    y=sh+dy[i]
    if x<0 or y<0 or x>=W or y>=H or seen[y][x] or S[y][x] == ".":
      continue
    dfs(y,x)

count=0
for i in range(H):
  for j in range(W):
    if seen[i][j] or S[i][j] == ".":
      continue
    else:
      count+=1
      dfs(i,j)
print(count)

      
  