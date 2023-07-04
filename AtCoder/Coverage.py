import itertools

N, M = map(int, input().split())
C = []
A = []
S = set()

# 数列Aをビット全探索
def judge(bit):
    for i in range(M):
        if bit[i]:# if文の判定では、0はFalse扱い、他の整数はTrue扱い
            S.update(A[i])

for i in range(M):
    C.append(int(input()))
    A.append(list(map(int, input().split())))

# タプルの「0 or 1」でビット列を表現
# N＝3なら3ビット
ans = 0
for bit in itertools.product((0,1), repeat = M):
    judge(bit)

    b = True
    for num in range(1, N+1):
        if num not in S:
            b = False
    
    if b:
        ans += 1
    S.clear()

print(ans)