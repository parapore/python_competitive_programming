n=int(input())
a=list(map(int,input().split()))

a.sort(reverse=True)

kisu=-1
gusu=-1

ans=-1
for i in range(n):
    if a[i]%2==0 and gusu != -1:
        ans=max(ans,a[i]+gusu)
    elif a[i]%2==0 and gusu == -1:
        gusu=a[i]
    elif a[i]%2==1 and kisu != -1:
        ans=max(ans,a[i]+kisu)
    elif a[i]%2==1 and kisu == -1:
        kisu=a[i]
print(ans)