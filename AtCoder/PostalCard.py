n, m = map(int, input().split())

s = []
for i in range(n):
    s.append(input())

t = set()
for i in range(m):
    t.add(input())

ans = 0
for i in s:
    for j in t:
        if i[3:] == j:
            ans += 1
                
print(ans)