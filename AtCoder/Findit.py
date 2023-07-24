n = int(input())
a = list(map(int, input().split()))
seen = [False]*n
ans = []
next = 0

cnt = 0
while not seen[next]:
    ans.append(next+1)
    seen[next]=True

    next = a[next]-1

# start = ans.index(next+1)

start = next+1
count = 0
while start != ans[count]:
    count+=1

print(len(ans[count:]))
print(*ans[count:])