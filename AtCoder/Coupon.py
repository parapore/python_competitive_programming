n,k,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)

for i in range(n):
    if k==0:
        break
    maisu = min(k, a[i] // x)
    a[i]=max(0, a[i]-maisu*x)
    k-=maisu

a.sort(reverse=True)
i=0
for i in range(n):
    if k == 0:
        break
    a[i]=0
    k-=1      

print(sum(a))