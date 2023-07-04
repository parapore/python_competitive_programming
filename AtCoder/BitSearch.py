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

#-------------------------------------------------------------------------------------------
# bit演算子を使うバージョン
N = 3
A=[1,2,3]

# 数列Aをビット全探索
def judge2(bit):
    for i in range(N):
        if(bit & (1 << i)):#整数bitを2進法とみなしたときの、下からi桁目が1か判定
            print(A[i], end=" ")
    print()

for bit in range(1 << N):#1~2のN乗
    print(bin(bit))
    judge2(bit)


