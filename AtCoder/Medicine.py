import sys
n, k = map(int, input().split())
ab = []

all = 0
for i in range(n):
    a, b = map(int, input().split())
    all += b
    ab.append((a, b))

ab.sort()

if all <= k:
    print(1)
    sys.exit()

for i in range(len(ab)):
    day = ab[i][0]
    kosu = ab[i][1]

    all -= kosu
    if all <= k:
        print(day+1)
        break

