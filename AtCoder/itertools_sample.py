import itertools

# 直積 ネストしたforループと同じ　0～2の数字の全通り。
# repeat=for文のネスト数と同じ。つまり数列の桁数。3*3*3=27
for product in itertools.product(range(0,3), repeat=3):
    print(product)
# 結果
# (0, 0, 0)
# (0, 0, 1)
# (0, 0, 2)
# (0, 1, 0)
# (0, 1, 1)
# (0, 1, 2)
# (0, 2, 0)
# (0, 2, 1)
# (0, 2, 2)
# (1, 0, 0)
# (1, 0, 1)
# (1, 0, 2)
# (1, 1, 0)
# (1, 1, 1)
# (1, 1, 2)
# (1, 2, 0)
# (1, 2, 1)
# (1, 2, 2)
# (2, 0, 0)
# (2, 0, 1)
# (2, 0, 2)
# (2, 1, 0)
# (2, 1, 1)
# (2, 1, 2)
# (2, 2, 0)
# (2, 2, 1)
# (2, 2, 2)

print()              

#順列=permutation 重複なし、順場違えば別の組み合わせ扱い。 3P3 = 3*2*1 = 3! = 6
for permutation in itertools.permutations(range(0,3)):
    print(permutation)
# (0, 1, 2)
# (0, 2, 1)
# (1, 0, 2)
# (1, 2, 0)
# (2, 0, 1)
# (2, 1, 0)

print()

#組み合わせ 重複なし。順番ちがくてもても同じ組み合わせ扱い。 3C3 = 3*2*1 / 3*2*1 = 1
for combination in itertools.combinations(range(0,3), 3):
    print(combination)
#(0, 1, 2)

print()

#組み合わせ 重複なし。順番ちがくてもても同じ組み合わせ扱い。 5C3 = 5*4*3 / 3*2*1 = 10
# 0~5の数字を3つ選ぶ
for combination in itertools.combinations(range(0, 5), 3):
    print(combination)
# (0, 1, 2)
# (0, 1, 3)
# (0, 1, 4)
# (0, 2, 3)
# (0, 2, 4)
# (0, 3, 4)
# (1, 2, 3)
# (1, 2, 4)
# (1, 3, 4)
# (2, 3, 4)

print()

#重複あり組み合わせ 重複あり。順番ちがくてもても同じ組み合わせ扱い。
for combination in itertools.combinations_with_replacement(range(3), 3):
    print(combination)
# (0, 0, 0)
# (0, 0, 1)
# (0, 0, 2)
# (0, 1, 1)
# (0, 1, 2)
# (0, 2, 2)
# (1, 1, 1)
# (1, 1, 2)
# (1, 2, 2)
# (2, 2, 2)

