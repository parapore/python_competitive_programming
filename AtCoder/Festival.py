import bisect

N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()

for i in range(1,N+1):
  index = bisect.bisect_left(A, i) #1　挿入できる値の左INDEXを返す
  if i==N:
    print(0)
  else:
    print(A[index] - i)