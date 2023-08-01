from collections import defaultdict

n,q=map(int, input().split())
#g=[set() for _ in range(n)] ここでTLEしてた
g=defaultdict(set)
tab=[list(map(int, input().split())) for _ in range(q)]

for i in range(q):
    a = tab[i][1]-1
    b = tab[i][2]-1

    if tab[i][0] == 1:
        g[a].add(b)

    elif tab[i][0] == 2:
        if b in g[a]:
            g[a].remove(b)

    else:
        if b in g[a] and a in g[b]:
            print("Yes")
        else:
            print("No")