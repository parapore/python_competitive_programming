from collections import defaultdict

#全て-1する用
def minus1(x):
    return int(x)-1

n=int(input())
a=defaultdict(list)#値、添字
aa=list(map(minus1, input().split()))
bb=list(map(minus1, input().split()))
cc=list(map(minus1, input().split()))

for i in range(n):
    ai=aa[i]
    a[ai].append(i)

ans=0
for j in range(n):
    if bb[cc[j]] in a:
        ans+=len(a[bb[cc[j]]])
print(ans)