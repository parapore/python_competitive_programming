# 動的計画法。あるご式。https://algo-method.com/descriptions/44


#すごろく
n,m=map(int, input().split())
d=list(map(int,input().split()))

dp=[False] * (n+1)
dp[0]=True

for i in range(1, n+1):
    for j in range(m):
        if i - d[j] >= 0 and dp[i-d[j]]:
            dp[i] = True

print("Yes" if dp[n] else "No")



#マスの移動２
n,m=map(int, input().split())
a=list(map(int,input().split()))

time=[10000000]*n
time[0]=0


for i in range(1,n):
    for j in range(1, m+1):
        if i-j >= 0:
            time[i] = min(time[i], time[i-j] + a[i]*j)

print(time[-1])

#タイルの敷き詰め
n=int(input())
p=[0]*(n+1)

p[0]=1

for i in range(1,n+1):
    if i-1>=0: p[i]+=p[i-1]
    if i-2>=0: p[i]+=p[i-2]
    if i-3>=0: p[i]+=p[i-3]

print(p[n])

# 階段の登り方
n=int(input())
pattern=[0]*(n+1)

pattern[0]=1
pattern[1]=1

for i in range(2,n+1):
    pattern[i] = pattern[i-1] + pattern[i-2]

print(pattern[n])


#マスの移動
n=int(input())
a=list(map(int,input().split()))
t=[0]*n

t[1]=a[1]
for i in range(2,n):
    t[i]=min(t[i-1]+a[i], t[i-2]+ a[i]*2)

print(t[n-1])

#数字の列
n,x,y=map(int,input().split())
a=[0]*n
a[0]=x
a[1]=y

#a[2~n]=(a[n-2]+a[n-1]) % 100
for i in range(2,n):
    a[i] = (a[i-2] + a[i-1]) % 100

print(a[n-1])