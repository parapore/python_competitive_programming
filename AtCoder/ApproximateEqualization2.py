n=int(input())
a=list(map(int,input().split()))
b=[]
sum=sum(a)
avg=sum//len(a)
amari=sum%len(a)
a.sort()
 
for i in range(n):
    b.append(avg)
 
 
for i in range(n-1, n-amari-1, -1):
    b[i]+=1
 
cnt=0
for i in range(n):
    cnt+=abs(a[i]-b[i])
 
print(cnt//2)



#全探索。余裕のTLEである。
# a.sort()
# b = True
# cnt=0
# while b:
#     cnt+=1
#     a[0]= a[0]+1
#     a[len(a)-1] = a[len(a)-1]-1
#     a.sort()
#     if a[0] +1 == a[len(a)-1]:
#         print(cnt)
#         b=True
#         exit()
