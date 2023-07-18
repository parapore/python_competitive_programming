s = input()
temp = s
ans = len(s)
while(len(temp) > 0):
    if len(temp) >= 2 and temp[-1] == "0" and temp[-2] == "0":
        ans -= 1
        temp = temp[:-2]
    else:
        temp = temp[:-1]
print(ans)   
