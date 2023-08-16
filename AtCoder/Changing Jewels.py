
import sys
sys.setrecursionlimit(10**6)

n,x,y=map(int,input().split())

def jwely(level, x, y, isRed):
    if level == 1:
        if isRed: return 0
        else: return 1     #1*x or 1*yが返却

    if isRed:
        return jwely(level-1, x, y, True) + jwely(level, x, y, False)*x
    else:
        return jwely(level-1, x, y, True) + jwely(level-1, x, y, False)*y

print(jwely(n,x,y,True))