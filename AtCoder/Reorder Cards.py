h,w,n=map(int, input().split())
a=[]
b=[]

for i in range(n):
    ai,bi=map(int,input().split())
    a.append(ai)
    b.append(bi)

#重複除去＆ソート
seta=sorted(set(a))
setb=sorted(set(b))

yranking={y: i+1 for i, y in  enumerate(seta)}
xranking={x: i+1 for i, x in  enumerate(setb)}

for i in range(n):
    ai =a[i]
    bi=b[i]

    print(yranking[ai],end=" ")
    print(xranking[bi])
