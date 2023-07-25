h,w=map(int, input().split())
slist=[input() for _ in range(h)]
tlist=[input() for _ in range(h)]
state=[[] for _ in range(w)]
ttate=[[] for _ in range(w)]

for i in range(w):
    for j in range(h):
        state[i].append(slist[j][i])
        ttate[i].append(tlist[j][i])

state.sort()
ttate.sort()

for i in range(w):
    ss = "".join(state[i])
    tt = "".join(ttate[i])
    if ss != tt:
        print("No")
        exit()
print("Yes")



