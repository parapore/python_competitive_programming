import sys
n = int(input())
ai = list(map(int, input().split()))

if 0 in ai:
    print(0)
    sys.exit()

ans = 1
for i in ai:
    ans *= i
    if ans > 1000000000000000000:
        print(-1)
        sys.exit()

print(ans)