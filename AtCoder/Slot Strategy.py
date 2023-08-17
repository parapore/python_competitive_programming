n=int(input())
s=[list(map(int,input())) for _ in range(n)]
numList=[[0]*10 for _ in range(10)]
maxList=[] 


for j in range(10):
    for k in range(n):
        num = s[k][j]
        numList[num][j]+=1

for i in range(10):
    maxd=0
    col=0
    for j in range(10):
        if maxd <= numList[i][j]:
            maxd=numList[i][j]
            col=j
    maxList.append([maxd,col])

maxList.sort()
ans=(maxList[0][0]-1)*10+maxList[0][1]#同じ列に重複があったら×１０秒
print(ans)

# 最初の解答。本当の全探索。
# def tatesearch(yoko, num):
#     for k in range(n):
#         if s[k][yoko] == str(num):
#             s[k][yoko] = "X"
#             return True
#     return False

# def yokosearch(num, seen, n):
#     time=0
#     for i in range(10):
#         time+=1
#         if tatesearch(i, num):
#             seen+=1
#             if seen == n:
#                 return seen, time
#     return seen, time 

# times=[]
# for i in range(10):
#     seen=0
#     time=0
#     while seen < n:
#         seen, ti =yokosearch(i, seen, n)
#         time+=ti
#     times.append(time-1)

# print(min(times))