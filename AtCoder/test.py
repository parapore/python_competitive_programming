
import math
import io
import sys
import os
os.system("Cls")
with open("HandInput.txt") as TxtOpen:
    INPUT = TxtOpen.read()
sys.stdin = io.StringIO(INPUT)
# --------------------------------------------------------
# 入力の受け取り
N=int(input())

# すでに使った数の記録
Used=[False]*(2*N+2)

# 最初は「1」を出力
print(1)

# 「1」は使用済み
Used[1]=True

# N回
for i in range(N+1):
    # 青木くんの入力を受け取り
    x=int(input())
    # 「x」は使った
    Used[x]=True

    # x=「0」の場合
    if x==0:
        # 終了
        exit()

    # k=1~(2k+1)
    for k in range(1,2*N+2):
        # まだ使っていないなら
        if Used[k]==False:
            # 「k」を出力
            print(k)
            # 「k」は使った
            Used[k]=True
            # forループを抜ける
            break
