from collections import defaultdict

n =int(input())
a =list(map(int, input().split()))

#重複削除
b = set()
for i in a:
    b.add(i)

memo=defaultdict(int)#値、出現回数
for ai in a:
    memo[ai]= memo[ai]+1

memo = sorted(memo.items(), reverse=True)
for k in range(n):
    if k < len(memo):
        print(memo[k][1])
    else:
        print(0)


