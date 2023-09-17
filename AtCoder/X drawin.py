N,A,B=map(int,input().split())
P,Q,R,S=map(int,input().split())
#グラフ作成
G=[["."]* (S-R+1) for _ in range(Q-P+1)]

#(A+k, B+k)
# P <= A+k <= Q and R <= B+k <= S
# 上記を満たす、最小のKは？
# P <= A+k → P-A <= k 
# R <= B+k → R-B <= k 
mink = max(P-A, R-B)
#最大
# A+k <= Q　→　k <= Q-A 
# B+k <= S  →  k <= S-B
maxk= min(Q-A, S-B)
for k in range(mink,maxk+1):
  G[A+k-P][B+k-R]="#"

# (A+k, B-k)
# P <= A+k <= Q and R <= B-k <= S:
# 上記を満たす、最小のKは？
# P <= A+k → P-A <= k  
# B-k <= S　→　-k <= -B+S　→　k >= B-S
mink = max(P-A, B-S)
#最大
# A+k <= Q　→　k <= Q-A 
# B+k <= S  →  k <= S-B
# R <= B-k　→　R-B <= -k　→　B-R >= k
maxk= min(Q-A, B-R)
for k in range(mink, maxk+1):
  G[A+k-P][B-k-R]="#"


for i in range(Q-P+1):
  for j in range(S-R+1):
    print(G[i][j], end="")
  print()