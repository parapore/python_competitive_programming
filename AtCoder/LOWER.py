n=int(input())
s=list(input())
q=int(input())
txc = []

for i in range(q):
    t, x, c = map(str, input().split())
    txc.append([t,x,c])
    if t != "1":
        index = i

for i in range(q):
    t,x,c = txc[i]
    t= int(t)
    x=int(x)
    if t==1:
        s[x-1] = c

    elif t==2 and i == index:
        s1="".join(s)
        s1=s1.lower()
        s=list(s1)
    elif t==3 and i ==index:        
        s1="".join(s)
        s1=s1.upper()
        s=list(s1)
print("".join(s))

