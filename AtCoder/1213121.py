import copy

n=int(input())

def S(n):
  if n == 1:
    return [1]
  else:
    return S(n - 1) + [n] + S(n - 1)

print(*S(n))

#別解
# if n==1:
#     print(1)
#     exit()

# sminus=[1]
# s=[]
# for i in range(n-1):
#     s.clear()
#     s.extend(sminus)
#     s.append(i+2)
#     s.extend(sminus)
#     sminus=copy.copy(s)
# print(*s)

