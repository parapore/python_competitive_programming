import random

f = open("C:\\Users\\jkoa7\\vscode_workspace\\python_competitive_programming\\AtCoder\\HandInput.txt", 'w')
n=random.randint(1,2*10**5)
x=random.randint(1,10**9)
y=random.randint(1,10**9)
f.write(str(n) +" "+str(x)+" "+str(y)+"\n")
print()
for i in range(n):
  f.write(str(random.randint(1,10**9)) + " ")