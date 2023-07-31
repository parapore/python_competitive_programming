# ok･･･条件を満たすなかで最小のindex。左側をOKにする
# ng･･･条件を満たさないなかで最大のindex。右側をNGにする
def is_ok2(i):
   return i <= 5

ok = 1 #左側(解が存在する値)
ng = 11 #右側(解が存在しない値)
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2 # 平均(小数切り捨て)
    if is_ok2(mid):
        ok = mid
    else:
    	ng = mid
print(ok,ng) # "5 6" が出力される

# ok･･･条件を満たすなかで最大のindex。右側をOKにする
# ng･･･条件を満たさないなかで最小のindex。左側をNGにする
def is_ok(i):
   return i > 5

ok = 10 #右側(解が存在する値)
ng = -1 #左側(解が存在しない値)
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2 # 平均(小数切り捨て)
    if is_ok(mid):
        ok = mid
    else:
    	ng = mid
print(ok,ng) # "6 5" が出力される


