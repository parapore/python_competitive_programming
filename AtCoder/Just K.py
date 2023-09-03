n,k=map(int,input().split())
Slist=[]

for i in range(n):
  si=input()
  S=set()
  for j in range(len(si)):
    S.add(si[j])
  Slist.append(S)

# 文字列Sリストをビット全探索
def judge2(bit):
  syurui=0
  for i in range(26):
    appearCnt=0
    alphbet = chr(ord("a") + i)
    #選択したSの中にa-zが含まれているか探索
    for j in range(n):
      if(bit & (1 << j)):
        if alphbet in Slist[j]:
          appearCnt+=1
    if appearCnt == k:
      syurui+=1
  return syurui
 
ans=0
for bit in range(1 << n):#1~2のN乗
    ans=max(ans, judge2(bit))
print(ans)