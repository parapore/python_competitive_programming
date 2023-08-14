from collections import defaultdict

x=list(input())
n=int(input())

#最初の解。文字列順に得点をつけて、得点が小さい順にソート
# tokuten=defaultdict(str)

# for i,s in enumerate(x):
#     tokuten[s]=i

# strs=[]
# for i in range(n):
#     si = input()
#     sils=list(si)
#     tokutenls=[]
#     for s in sils:
#         tokutenls.append(tokuten[s])
        
#     strs.append((si, tokutenls))

# strs=sorted(strs, key=lambda a: a[1] )
# for i in strs:
#     print(i[0])



# ソート関数を実装するパターン
from functools import cmp_to_key
# 比較対象の2つの値を引数とし、第一引数が第二引数よりも小さければ負の値、大きければ正の値、等しければ0を返すように実装します。
def compare(arg1, arg2):
    length = min(len(arg1), len(arg2))
    for i in range(length):
            # if x.index(arg1[i]) == x.index(arg2[i]): return 0
            if x.index(arg1[i]) < x.index(arg2[i]): return -1
            if x.index(arg1[i]) > x.index(arg2[i]): return 1
    if len(arg1) == len(arg2):
        return 0
    elif len(arg1) < len(arg2):
        return -1
    else:
         return 1         

strs=[]
for i in range(n):
    strs.append(input())

strs = sorted(strs, key=cmp_to_key(compare))
for i in strs:
     print(i)