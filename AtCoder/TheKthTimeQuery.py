from collections import defaultdict

n,q=map(int,input().split())
a=list(map(int,input().split()))
xk=[]
ai=defaultdict(list)#値,出現場所

for i in range(n):
    ai[a[i]].append(i)

for i in range(q):
    x,k=map(int, input().split())
    syutugenbasyo = ai[x]
    if len(syutugenbasyo) < k:
        print(-1)
    else:
        print(syutugenbasyo[k-1]+1)
