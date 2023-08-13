
# bit演算子を使うバージョン
s=list(input())
s.sort(reverse=True)
N=len(s)

# 数列をビット全探索
def judge2(bit,mutiply):
    t1=[]
    t2=[]
    for i in range(N):
        if(bit & (1 << i)):#整数bitを2進法とみなしたときの、下からi桁目が1か判定
            t1.append(s[i])
        else:
            t2.append(s[i])
        # t1.sort(reverse=True)
        # t2.sort(reverse=True)

    if len(t1)==0 or len(t2) == 0:
        return 0
    mutiply = int("".join(t1)) * int(("".join(t2)))
    
    # 旧回答。この中で順列全探索。
    # #順列=permutation 重複なし、順場違えば別の組み合わせ扱い。 3P3 = 3*2*1 = 3! = 6
    # for permutation in itertools.permutations(t1):
    #     for pemutation2 in itertools.permutations(t2):

    #         if permutation[0] == 0 or pemutation2[0] == 0:
    #             continue
    #         mutiply = max(int("".join(permutation)) * int("".join(pemutation2)), mutiply)

    return mutiply

ans = 0
for bit in range(1 << N):#2のN乗
    ans = max(ans, judge2(bit, 0))

print(ans)