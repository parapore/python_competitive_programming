from collections import defaultdict

n=int(input())
s=defaultdict(str)

for i in range(n):
    si=input()
    if si in s:
        times=s[si]
        s[si]=times+1
        print(si+"("+ str(times+1) +")")
    else:
        print(si)
        s[si]=0
    
