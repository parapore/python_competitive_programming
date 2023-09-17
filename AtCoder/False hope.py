
# --------------------------------------------------------
import itertools

C=[list(map(int,input().split())) for _ in range(3)]
count = 0
for permutation in itertools.permutations(range(0,9)):
    Copen=[[i*3+10+j for j in range(3)] for i in range(3)]
    flag=[[False,False,False] for i in range(3)]
    
    for i in range(9):
      
      openNo = permutation[i]
      flag[openNo // 3][openNo % 3] = True
      num = C[openNo // 3][openNo % 3]
      Copen[openNo // 3][openNo % 3] = num

      
      #左縦
      if (Copen[0][0] == Copen[1][0] and flag[2][0] == False) or (Copen[0][0] == Copen[2][0] and flag[1][0] == False) or (Copen[1][0] == Copen[2][0]  and flag[0][0] == False):
        count+=1
        break
      #真ん中縦
      if (Copen[0][1] == Copen[1][1] and flag[2][1] == False) or (Copen[0][1] == Copen[2][1] and flag[1][1] == False) or (Copen[1][1] == Copen[2][1] and flag[0][1] == False):
        count+=1
        break
      #右縦
      if (Copen[0][2] == Copen[1][2] and flag[2][2] == False) or (Copen[0][2] == Copen[2][2] and flag[1][2] == False) or (Copen[1][2] == Copen[2][2] and flag[0][2] == False):
        count+=1
        break
      #上横
      if (Copen[0][0] == Copen[0][1] and flag[0][2] == False) or (Copen[0][0] == Copen[0][2] and flag[0][1] == False) or (Copen[0][1] == Copen[0][2] and flag[0][0] == False):
        count+=1
        break
      #真ん中横
      if (Copen[1][0] == Copen[1][1] and flag[1][2] == False) or (Copen[1][0] == Copen[1][2] and flag[1][1] == False) or (Copen[1][1] == Copen[1][2] and flag[1][0] == False):
        count+=1
        break
      #下横
      if (Copen[2][0] == Copen[2][1] and flag[2][2] == False) or (Copen[2][0] == Copen[2][2] and flag[2][1] == False) or (Copen[2][1] == Copen[2][2] and flag[2][0] == False):
        count+=1
        break
      #斜め左上から
      if (Copen[0][0] == Copen[1][1] and flag[2][2] == False) or (Copen[0][0] == Copen[2][2] and flag[1][1] == False) or (Copen[1][1] == Copen[2][2] and flag[0][0] == False):
        count+=1
        break
      #斜め右上から
      if (Copen[0][2] == Copen[1][1] and flag[2][0] == False) or (Copen[0][2] == Copen[2][0] and flag[1][1] == False) or (Copen[1][1] == Copen[2][0] and flag[0][2] == False):
        count+=1
        break

print(1 - count / 362880)
      






