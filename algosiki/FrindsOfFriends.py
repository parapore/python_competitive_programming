n ,m, x = map(int, input().split())
ab = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    ab[a].append(b)
    ab[b].append(a)

friends = set()
for i in range(1, n):
    if i in ab[x]:#アルルと直接友達か？
        for j in ab[i]:#アルルの友達の友達を全探索
            if j not in ab[x] and j != x: #アルルの友達の友達が、アルルと直接友達ではないならOK
                friends.add(j)
print(len(friends))