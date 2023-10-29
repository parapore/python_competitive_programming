import bisect

N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()

ans=0
for i in range(N):
  ans = max(bisect.bisect_right(A, A[i]+M-1) -i, ans) 

print(ans)