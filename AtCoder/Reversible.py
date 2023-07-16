n = int(input())
s = set()
 
for i in range(n):
        ss = input()
        if ss[::-1] in s:
              continue
        s.add(ss)
 
print(len(s))