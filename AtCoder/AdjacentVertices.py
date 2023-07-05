n, m = map(int, input().split())
g = [[] for _ in range(5)]
print(g)

for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    

for i in range(n):
    ans = ""
    ans += str(i+1) + ": {"    
    for j in range(len(g[i])):
        if j != len(g[i]) -1:
            ans += str(g[i][j]+1) + ", "
        else:
            ans += str(g[i][j]+1)
    print(ans + "}")
