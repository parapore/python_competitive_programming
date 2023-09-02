n,d,p=map(int,input().split())
f=list(map(int, input().split()))
f.sort(reverse=True)

total=sum(f)
subtotal=0
for i in range(n):
  cnt+=1
  subtotal+=f[i]
  if (cnt == d) or i == n-1:
    if subtotal >= p:
      total+=p
      total-=subtotal
    else:
      break
    subtotal=0
    cnt=0
  
print(total)


#最初の解答
# subtotal=0
# pas=0
# cnt=0
# for i in range(n):
#   cnt+=1
#   subtotal+=f[i]
#   if (cnt == d) or i == n-1:
#     if subtotal >= p:
#       pas+=1
#     else:
#       break
#     subtotal=0
#     cnt=0
  

# #パスは
# if pas*d >= n:
#   print(pas*p)
#   exit()

# i = max(0, i-cnt+1)#REしてそう
# ans = pas*p
# for j in range(i,n):
#   ans+=f[j]
# print(ans)