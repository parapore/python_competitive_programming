from collections import defaultdict
import math
import io
import sys
import os
os.system("Cls")
with open("C:\\Users\\jkoa7\\vscode_workspace\\python_competitive_programming\\AtCoder\\HandInput.txt") as TxtOpen:
    INPUT = TxtOpen.read()
sys.stdin = io.StringIO(INPUT)
# --------------------------------------------------------
n = int(input())
a = list(map(int, input().split()))

count = defaultdict(int)

for i in range(n):
    count[a[i]] += 1

#全組み合わせ数　nC2
ans = n * (n-1) // 2

for x in count.values():

    #重複組合せ数を引く
    ans -= x * (x-1) // 2

print(ans)

