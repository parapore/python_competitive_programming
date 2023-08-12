#前後aなしが回分かつ前のaが後ろのaより少ないこと
# rstrip("a") lstrip("a")とs == s[::-1]を使えばもっと楽に解けた。
s=list(input())

start=0
end=len(s)-1
sacnt=0
eacnt=0
for _ in range(len(s)):
  atama=s[start]
  matubi = s[end]
  if atama=="a":
    start+=1
    sacnt+=1
  if matubi=="a":
     end-=1
     eacnt+=1


if sacnt>eacnt:
   print("No")
   exit()

ans=True
while start < end:
  if s[start] != s[end]:
    ans=False
    break
  start+=1
  end-=1

if ans:
   print("Yes")
else:
   print("No")

