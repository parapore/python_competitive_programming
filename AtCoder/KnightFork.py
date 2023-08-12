x,y,x2,y2=map(int,input().split())

dx=[1,2, 2, 1,-1,-2,-2,-1]
dy=[2,1,-1,-2 ,2 ,1,-1,-2]

ls1=[]
ls2=[]

for i in range(8):
    xx=x+dx[i]
    yy=y+dy[i]

    xx2=x2+dx[i]
    yy2=y2+dy[i]

    ls1.append((xx,yy))
    ls2.append((xx2,yy2))

for i in ls1:
    for j in ls2:
        if i==j:
            print("Yes")
            exit()
print("No")