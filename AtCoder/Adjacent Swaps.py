from collections import defaultdict

n,q=map(int, input().split())
#連想配列Key=値　VALUE=並び順
MAP=defaultdict(int)
#配列、値と並び順再現用
xls=[]

for i in range(n):
  xls.append(i)
  MAP[i]=i

for i in range(q):
  xi = int(input())-1
  #連想配列でXを指定して並び順を取得。
  narabijun = MAP[xi]

  #並び順配列から、隣の値を取得。
  if narabijun == len(xls)-1:
    tonariValue = xls[narabijun-1]
    index = -1
  else:
    tonariValue = xls[narabijun+1]
    index = 1

  #隣と値交換
  xls[narabijun], xls[narabijun+index] = xls[narabijun+index], xls[narabijun]
  MAP[tonariValue] = narabijun
  MAP[xi] = narabijun+index

for i in xls:
  print(i+1, end=" ")