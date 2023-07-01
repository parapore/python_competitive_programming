n = int(input())
a = list(map(int, input().split()))
q = int(input())

for i in range(q):
    qu = list(map(int, input().split()))
    if qu[0] == 1:
        a[qu[1]-1] = qu[2]
    else:
        print(a[qu[1]-1])