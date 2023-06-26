# import：import itertolls
import itertools

#int
N=int(input())
A,B=map(int, input().split())

#文字列
S=input()
S,T=map(str, input().split())

#list
A=list(map(int, input().split()))
 
N,K=4,2
 
# 順列：permutations(range(N))
# seq=(0,1,2,3),(0,1,3,2),(0,2,1,3),(0,2,3,1),...,(3,2,1,0)
print("[順列]")
for seq in itertools.permutations(range(N)):
    print(seq)
 
# 重複なしの組み合わせ：combinations(range(N),K)
print("[重複なしの組み合わせ]")
# seq=(0,1),(0,2),(0,3),(1,2)...,(2,3)
for seq in itertools.combinations(range(N),K):
    print(seq)
 
# 重複ありの組み合わせ：combinations_with_rep(range(N),K)
print("[重複ありの組み合わせ]")
# seq=(0,0),(0,1),(0,2),(0,3),(1,1)...,(3,3)
for seq in itertools.combinations_with_replacement(range(N),K):
    print(seq)
 
# 直積：product(range(N),range(N)):
print("[直積]")
# seq=(0,0),(0,1),(0,2),(0,3),(1,0)...,(3,3)
for seq in itertools.product(range(N),range(N)):
    print(seq)
