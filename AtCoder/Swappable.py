from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

count = defaultdict(int)

for i in range(n):
    count[a[i]] += 1

#全組み合わせ数　nC2
ans = n * (n-1) // 2

for x in count.values():

    #重複組合せ数を引く
    ans -= x * (x-1) // 2

print(ans)

