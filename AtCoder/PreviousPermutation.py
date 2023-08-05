n=int(input())
p=list(map(int, input().split()))
p2=[]

#分岐点を調べるp-1 > p
#分岐点までの数列をp2にストックする
#分岐点の値をbunkiに持っておく
#分岐点1つ前の添字番号もbeforebunkindexに持っておく
beforebunkindex=0
bunki=0
for i in range(n-1,0,-1):
    p2.append(p[i])
    if p[i-1] > p[i]:
        p2.append(p[i-1])
        beforebunkindex = i-2
        bunki=p[i-1]
        break

#ストックをソートする
#分岐点の値より１つ小さい値をストックから探す
bunkiValue=0
p2 = sorted(p2, reverse=True)
for i in range(len(p2)):
    if bunki > p2[i]:
        bunkiValue = p2[i]
        break


#分岐前までを出力
for i in range(0, beforebunkindex+1):
    print(p[i], end=" ")

#分岐点の値より1つ小さい値を出力＆削除
print(bunkiValue, end=" ")
p2.remove(bunkiValue)

#ストックを大きい順に出力
p2.sort(reverse=True)
print(*p2)