import itertools

n=int(input())
nisin=format(n,'b')
jusin=int(nisin,2)
dokoga1=[-1]*15

#maxnisin="1000000000000000000000000000000000000000000000000000000000000"
maxnisin=["0"]*60

#2進数の何桁目が1か探索
cnt=0
for i in range(len(nisin)):
    if nisin[len(nisin)-1-i] == "1":
        dokoga1[cnt]=i
        cnt+=1
        
if cnt==0:
    print(0)
    exit()

#部分集合になる全通りの２進数を作る。最大2の１５乗
ans=[]
for product in itertools.product(range(0,2), repeat=cnt):
    maxnisin=["0"]*60
    for i in range(cnt):
        if product[i] == 1:
            iti = 69 - dokoga1[i]
            maxnisin[iti] = "1"
    s= "".join(maxnisin)
    ans.append(int(s,2))

ans.sort()
for i in ans:
    print(i)