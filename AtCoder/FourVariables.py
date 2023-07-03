# N の約数をすべて求める関数
def calc_divisors(N):
    # 答えを表す集合
    res = []

    # 各整数 i が N の約数かどうかを調べる
    for i in range(1, N + 1):
        # √N で打ち切り
        if i * i > N:
            break
        
        # i が N の約数でない場合はスキップ
        if N % i != 0:
            continue

        # i は約数である
        res.append(i)

        # N ÷ i も約数である (重複に注意)
        if N // i != i:
            res.append(N // i)

    # 約数を小さい順に並び替えて出力
    res.sort()
    return res

n = int(input())

count = 0
for ab in range(1, n+1):
    ab1 = calc_divisors(ab)
    cd1 = calc_divisors(n-ab)

    count += len(ab1) * len(cd1)

print(count)