n,x=map(int,input().split())
dp=[[False]*(x+1) for _ in range(n+1)]# [ジャンプ数][座標]。

dp[0][0]=True
for i in range(n):
    a, b = map(int, input().split())
    for j in range(x):
        if dp[i][j]:
            if j+a <= x:
                dp[i+1][j+a] = True
            if j+b <= x:
                dp[i+1][j+b] = True

if dp[n][x]:
    print("Yes")
else:
    print("No")