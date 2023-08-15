from collections import defaultdict

n,k=map(int,input().split())
ab=defaultdict(int)#村、金
for i in range(n):
    a,b=map(int, input().split())
    ab[a]+=b

ab = sorted(ab.items(), key=lambda x: x[0], reverse=True)

genzai=0
while k > 0:
    if len(ab) > 0 and k + genzai >= ab[len(ab)-1][0]:
        k -= ab[len(ab)-1][0] - genzai
        k += ab[len(ab)-1][1]
        genzai = ab[len(ab)-1][0]
        ab.pop()
    else:
        genzai += k
        k=0
print(genzai)

