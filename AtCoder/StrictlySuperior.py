n , m = map(int, input().split())#商品数、機能数
pcf = [list(map(int, input().split())) for _ in range(n)]
PF = []# priceとfunction


for price, c, *func in pcf: #アンパック
    PF.append([price, set(func)])# List<intとSetの複合>

b = False
for i in range(n):
    for j in range(n):
        if i == j:
            continue

        flag1 = False
        if PF[i][0] >= PF[j][0] and PF[i][1] < PF[j][1]:
            print("Yes")
            exit()

        flag2 = False
        if PF[i][0] > PF[j][0]  and PF[i][1] <= PF[j][1]:
            print("Yes")
            exit()
print("No")