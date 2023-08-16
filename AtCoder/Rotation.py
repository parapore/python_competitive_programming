n,q=map(int, input().split())
s=list(input())
soeji=[i for i in range(n)]

shiftCnt=0
starts= 0
for i in range(q):
    a,b=map(int,input().split())
    if a==1:
        shiftCnt+=b
    else:
        b = (b-1-shiftCnt) % n
        if b == 0:
            print(s[0])
        else:
            print(s[b])