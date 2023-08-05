from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

#解法１
n=int(input())
ai=list(map(int, input().split()))
ameba=defaultdict(int)#アメーバ番号、世代数

for i, parent in enumerate(ai):
    child1 = (i+1)*2
    child2 = (i+1)*2+1
    ameba[child1]= ameba[parent]+1
    ameba[child2]= ameba[parent]+1

for i in ameba.values():
    print(i, end=" ")

#解法２
#有向グラフで作る
n=int(input())
ai=list(map(int, input().split()))
ameba=defaultdict(list)
depthdict=defaultdict()

for i in range(n):
    child1=(i+1)*2
    child2=(i+1)*2+1
    
    ameba[ai[i]].append(child1)
    ameba[ai[i]].append(child2)

#{頂点：深さ}で保存しておく
def dfs(v,depth):
    depth+=1
    depthdict[v]=depth
    for next in ameba[v]:
        dfs(next, depth)
    return

dfs(1,0)

#親の深さを調べる
print(0,end=" ")
for i in ai:
    ans = depthdict[i]
    print(ans, end=" ")
    print(ans, end=" ")