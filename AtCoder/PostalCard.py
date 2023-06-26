n, m = map(int, input().split())

s = []
for i in range(n):
    s.append(input())

t = []
for i in range(m):
    t.append(input())

ans = 0
for i in range(n):
    for j in range(m):
        for k in range(3, 6):
            b = True
            if s[i][k] != t[j][k-3]:
                b = False
                break

        if b == True:
                ans += 1
                break
                
print(ans)