h,w=map(int, input().split())
g = [input() for _ in range(h)]
seen=[[False] * w for _ in range(h)]

y=0
x=0
while(True):
        if seen[y][x]:
            print(-1)
            exit()

        seen[y][x]=True

        tempy=y
        tempx=x
        now = g[y][x]
        if now == "U":
            y-=1
        elif now == "D":
            y+=1
        elif now == "L":
            x-=1
        else:
            x+=1
        
        if y >= h or y < 0 or x >= w or x < 0:
            print(str(tempy+1) + " " + str(tempx+1))
            exit()
