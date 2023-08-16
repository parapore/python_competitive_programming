s=input()
t=input()

temps=s[0]
tempt=t[0]
if temps != tempt:
    print("No")
    exit()

sls=[]
prevs=0
for i in range(len(s)):
    if temps != s[i]:
        length = i - prevs
        sls.append([temps, length])
        prevs=i
        temps=s[i]
#最後の1文字
sls.append([temps, i - prevs+1])

tls=[]
prevt=0
for i in range(len(t)):
    if tempt != t[i]:
        length = i - prevt
        tls.append([tempt, length])
        prevt=i
        tempt=t[i]
#最後の1文字
tls.append([tempt, i - prevt+1])

if len(sls) != len(tls):
    print("No")
    exit()

for i in range(len(sls)):
    if sls[i][0] != tls[i][0]:
        print("No")
        exit()
    
    if (sls[i][1] == 1 and tls[i][1] > 1) or (sls[i][1] > tls[i][1]):
        print("No")
        exit()
print("Yes")