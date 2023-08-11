n=int(input())
cnt=0
maxPoint=0
s=set()

for i in range(n):
    si,ti=input().split()
    ti=int(ti)

    if si not in s:
        if ti > maxPoint:
            maxPoint=ti
            cnt=i+1
    s.add(si)
print(cnt)