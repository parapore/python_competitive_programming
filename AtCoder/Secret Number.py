import itertools

s=input()
must=set()
no=set()
for i in range(10):
    if s[i] == "o":
        must.add(i)
    if s[i] == "x":
        no.add(i)


# 直積 ネストしたforループと同じ　0～2の数字の全通り。
# repeat=for文のネスト数と同じ。つまり数列の桁数。3*3*3=27
ans=0
for product in itertools.product(range(0,10), repeat=4):
    pset=set(product)
    if must <= pset and no.isdisjoint(pset):
        ans+=1
print(ans)