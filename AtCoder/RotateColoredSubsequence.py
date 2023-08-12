from collections import defaultdict
import copy

n,m=map(int,input().split())
s=list(input())
s2=copy.copy(s)
c=list(map(int,input().split()))

color=defaultdict(list)
#連想配列に文字色：添字番号
#文字列を入れ替え
for i in range(n): 
    color[c[i]-1].append(i)

for i in range(m):
    cls = color[i]
    if len(cls) == 1:
        continue
    for j in range(len(cls)):
        if j == len(cls)-1:
            s[cls[0]] = s2[cls[j]]
        else:
            s[cls[j+1]]=s2[cls[j]]
print(*s, sep="")