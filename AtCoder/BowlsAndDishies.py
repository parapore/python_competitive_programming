n, m = map(int, input().split())
ab = []
for i in range(m):
    ab.append(list(map(int,input().split())))

k = int(input())
cd = []
for i in range(k):
    cd.append(list(map(int, input().split())))

s = set()
def bitSearch(bit):
    for i in range(k):
        if bit & (1 << i):
            s.add(cd[i][1])
        else:
            s.add(cd[i][0])

def check():
    count = 0
    for i in range(m):
        if ab[i][0] in s and ab[i][1] in s:
            count += 1
    return count

ans = 0
for bit in range(1 << k):
    bitSearch(bit)
    ans = max(ans, check())
    s.clear()

print(ans)


        

