#全探索
# https://dodosu.hatenablog.jp/entry/2023/06/26/172535
import itertools

#int
N=int(input())
A,B=map(int, input().split())

#文字列
S=input()
S,T=map(str, input().split())

#list
A=list(map(int, input().split()))
 
N,K=4,2
 
# 順列：permutations(range(N))
# seq=(0,1,2,3),(0,1,3,2),(0,2,1,3),(0,2,3,1),...,(3,2,1,0)
print("[順列]")
for seq in itertools.permutations(range(N)):
    print(seq)
 
# 重複なしの組み合わせ：combinations(range(N),K)
print("[重複なしの組み合わせ]")
# seq=(0,1),(0,2),(0,3),(1,2)...,(2,3)
for seq in itertools.combinations(range(N),K):
    print(seq)
 
# 重複ありの組み合わせ：combinations_with_rep(range(N),K)
print("[重複ありの組み合わせ]")
# seq=(0,0),(0,1),(0,2),(0,3),(1,1)...,(3,3)
for seq in itertools.combinations_with_replacement(range(N),K):
    print(seq)
 
# 直積：product(range(N),range(N)):
print("[直積]")
# seq=(0,0),(0,1),(0,2),(0,3),(1,0)...,(3,3)
for seq in itertools.product(range(N),range(N)):
    print(seq)

#-----------------------------------------------------------------------
# 約数列挙
# N の約数をすべて求める関数
def calc_divisors(N):
    # 答えを表す集合
    res = []

    # 各整数 i が N の約数かどうかを調べる
    for i in range(1, N + 1):
        # √N で打ち切り
        if i * i > N:
            break
        
        # i が N の約数でない場合はスキップ
        if N % i != 0:
            continue

        # i は約数である
        res.append(i)

        # N ÷ i も約数である (重複に注意)
        if N // i != i:
            res.append(N // i)

    # 約数を小さい順に並び替えて出力
    res.sort()
    return res

# ここに約数の数を知りたい数字を入れる
print(calc_divisors(9))
#------------------------------------------------------
#bit全探索
N = 3
A=[1,2,3]

# 数列Aをビット全探索
def judge(bit):
    total = 0
    for i in range(N):
        if bit[i]:# if文の判定では、0はFalse扱い、他の整数はTrue扱い
            print(A[i], end=" ")
    print()

# タプルの「0 or 1」でビット列を表現
# N＝3なら3ビット
for bit in itertools.product((0,1), repeat=N):
    print(bit)
    judge(bit)

#-------------------------------------------------------------------------------------------
# bit演算子を使うバージョン
N = 3
A=[1,2,3]

# 数列Aをビット全探索
def judge2(bit):
    for i in range(N):
        if(bit & (1 << i)):#整数bitを2進法とみなしたときの、下からi桁目が1か判定
            print(A[i], end=" ")
    print()

for bit in range(1 << N):#1~2のN乗
    print(bin(bit))
    judge2(bit)
#--------------------------------------------------------------------
#DFS
# https://dodosu.hatenablog.jp/entry/2023/05/20/131449#Python

import sys
sys.setrecursionlimit(10**6)# これ入れないと再帰回数オーバーでREになる

# 標準入力受け取り
n, m = map(int, input().split())
g = [[] for _ in range(n)]
seen = [False]*n

# 標準入力を2次元配列g（グラフ）で受け取り
for i in range(m):
    a, b = map(int, input().split())#aが頂点、bが辺を表す
    g[a-1].append(b-1)
    g[b-1].append(a-1)


def dfs(num):
    seen[num] = True
    for next in g[num]:
        if seen[next]:
            continue
        dfs(next)

dfs(0)

if sum(seen) == n:
    print("The graph is connected.")
else:
    print("The graph is not connected.")

#----------------------------------------------------------------------
#BFS 幅優先探索
# 経路復元＆距離計測つき

from collections import deque

n,x,y=map(int, input().split())
g=[[] for _ in range(n)]
Q=deque()
seen=[False]*n #探索済チェック用
dist=[0]*n #距離計測用
previous =[0]*n #探索経路用

#入力の受け取り
for i in range(n-1):
    u,v=map(int,input().split())
    u=u-1
    v=v-1
    g[u].append(v)
    g[v].append(u)

Q.append(0)#始点をキューに追加
previous[0] = -2 #始点には-2
while(len(Q)) > 0:
    vertex = Q.popleft() #先入れ先出し
    #vertex = Q.pop #後入れ先出し
    seen[vertex] = True

    for next in g[vertex]:
        if seen[next]: continue #探索済みはスルー
            
        dist[next] = dist[vertex] + 1 #距離を格納

        #探索経路を1つ前の頂点を追加
        previous[next] = vertex

        Q.append(next)#キューに次を追加

ans = []
now = 5 #頂点5から始点までの最短経路復元
ans.append(now)
while previous[now] != -2:
    now = previous[now]
    ans.append(now + 1)

# 最短経路を出力
print(*ans[::-1])

#----------------------------------------------------------------------
#2分探索
# ok･･･条件を満たすなかで最大のindex。左側をOKにする
# ng･･･条件を満たさないなかで最小のindex。右側をNGにする
def is_ok2(i):
   return i <= 5

ok = 1 #左側(解が存在する値)
ng = 11 #右側(解が存在しない値)
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2 # 平均(小数切り捨て)
    if is_ok2(mid):
        ok = mid
    else:
    	ng = mid
print(ok,ng) # "5 6" が出力される

# ok･･･条件を満たすなかで最小のindex。右側をOKにする
# ng･･･条件を満たさないなかで最大のindex。左側をNGにする
def is_ok(i):
   return i > 5

ok = 10 #右側(解が存在する値)
ng = -1 #左側(解が存在しない値)
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2 # 平均(小数切り捨て)
    if is_ok(mid):
        ok = mid
    else:
    	ng = mid
print(ok,ng) # "6 5" が出力される