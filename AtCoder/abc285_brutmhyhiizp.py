s = input()
temp = s

ans = 0
for i in range(len(s)):
    # 末尾をASCIIコードに変換 
    asciiCode = ord(temp[-1]) - ord('A') +1

    # アルファベット26文字なので26進数
    num2 = pow(26, i)
    ans += num2 * asciiCode

    #末尾を削除
    temp = temp[0:-1]
print(ans)