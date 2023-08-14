n,m=map(int,input().split())
a=[list(input()) for _ in range(2*n)]
katiban=[[0,i] for i in range(2*n)]
#勝ち数,番号で毎回ソート
for i in range(m):
    katiban = sorted(katiban, key=lambda a: (-a[0], a[1]))
    for j in range(0,2*n,2):
        ban1 = katiban[j][1]
        ban2 = katiban[j+1][1]
        ja1 = a[ban1][i]
        ja2 = a[ban2][i]

        if ja1 == "G" and ja2 == "C":
            katiban[j][0]+=1
        elif ja1 == "C" and ja2 == "P":
            katiban[j][0]+=1
        elif ja1 == "P" and ja2 == "G":
            katiban[j][0]+=1
        elif ja1 == ja2:
            abc=1
        else:
            katiban[j+1][0]+=1

katiban = sorted(katiban, key=lambda a: (-a[0], a[1]))
for i in range(n*2):
    print(katiban[i][1]+1)