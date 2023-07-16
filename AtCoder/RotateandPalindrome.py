n,a,b = map(int, input().split())
s = input()
ans = 0

for i in range(n):
    left = 0
    right = len(s)-1
    difCount = 0
    # 回分チェック
    while left < right:
        if s[left] != s[right]:
            difCount += 1
        left+=1
        right-=1

    if i == 0:
        ans = b*difCount
    else:
        ans = min(ans, a*i + b*difCount)
    s = s[1:n] + s[0]#文字列操作

print(ans)