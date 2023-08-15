from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
amaripattern=defaultdict(int)#余り、個数

for i in range(n):
    amari = a[i] % 200
    amaripattern[amari]+=1

ans=0
for i in amaripattern.values():
    if i != 1:
        ans+=i*(i-1) // 2
print(ans)


