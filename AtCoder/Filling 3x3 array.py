import itertools

h1,h2,h3,w1,w2,w3 = map(int,input().split())
ans=0
for product in itertools.product(range(1,29), repeat=4):
    leftup=product[0]
    rightup=product[1]
    leftunder=product[2]
    rightunder=product[3]

    p31=h1 - leftup - rightup
    p32=h2 - leftunder - rightunder
    p13=w1 - leftup - leftunder
    p23=w2 - rightup - rightunder
    p33_h= h3 - p13 - p23
    p33_w= w3 - p31 - p32

    if min(p31,p32,p33_h,p13,p23,p33_w) < 1:
        continue

    if p33_h == p33_w:
        ans+=1
print(ans)