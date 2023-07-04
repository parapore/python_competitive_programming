import itertools
N = 3
A=[1,2,3]

# 数列Aをビット全探索
def judge(bit):
    total = 0
    for i in range(N):
        if bit[i]:# if文の判定では、0はFalse扱い、他の整数はTrue扱い
            print(A[i], end=" ")
    print()

# タプルの「0 or 1」でビット列を表現
# N＝3なら3ビット
for bit in itertools.product((0,1), repeat=N):
    print(bit)
    judge(bit)
