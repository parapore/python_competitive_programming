import itertools
s, k = map(str, input().split())
k = int(k)

sset = set()

ss = ""
for p in itertools.permutations(s):
    for i in range(len(p)):
        ss += p[i]
    sset.add(ss)
    ss = ""

list = []
for i in sset:
    list.append(i)

list.sort()

print(list[k-1])
