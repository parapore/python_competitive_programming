from collections import defaultdict

n=int(input())
xy=[list(map(int, input().split())) for _ in range(n)]
lrs=list(input())
for i in range(n):
    xy[i].append(lrs[i])

yKey=defaultdict(list)#Y座標,ｘ座標・LR
for i in range(n):
    x,y,lr = xy[i]
    yKey[y].append([x, lr])

for values in yKey.values():
    isR=False
    values.sort()
    for value in values:
        if value[1] == "R":
            isR=True
        if value[1] == "L" and isR:
            print("Yes")
            exit()
print("No")