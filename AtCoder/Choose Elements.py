n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

dp=[[False]*n for _ in range(2)]

dp[0][0]=True
dp[1][0]=True

for i in range(1,n):
    #a[i-1]がTrueなら、a[i]へいけるか、b[i]へ行けるかを考える
    if dp[0][i-1]:
        #a[i-1]からa[i]へいけるか？
        if abs(a[i-1] - a[i]) <= k:
            dp[0][i] = True
        #a[i-1]からb[i]へいけるか？
        if abs(a[i-1] - b[i]) <= k:
            dp[1][i] = True

    #b[i-1]がTrueなら、a[i]へいけるか、b[i]へ行けるかを考える
    if dp[1][i-1]:
        #b[i-1]からa[i]へいけるか？
        if abs(b[i-1] - a[i]) <= k:
            dp[0][i] = True
        #b[i-1]からb[i]へいけるか？
        if abs(b[i-1] - b[i]) <= k:
            dp[1][i] = True



if dp[0][n-1] or dp[1][n-1]:
    print("Yes")
else:
    print("No")