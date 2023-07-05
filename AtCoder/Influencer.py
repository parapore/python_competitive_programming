n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

max1 = 0
ans = 0
for i in range(n):
    if len(g[i]) > max1:
        max1 = len(g[i])
        ans = i+1
print(ans)