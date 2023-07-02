from decimal import Decimal
from collections import defaultdict
import itertools
import math
import io
import sys
import os
import re
os.system("Cls")
with open("C:\\Users\\jkoa7\\vscode_workspace\\python_competitive_programming\\AtCoder\\HandInput.txt") as TxtOpen:
    INPUT = TxtOpen.read()
sys.stdin = io.StringIO(INPUT)
# --------------------------------------------------------
from fractions import Fraction
n = int(input())
ab = []
for i in range(n):
    a, b = map(Fraction, input().split())
    ab.append((a / (a+b), i))  # タプルをリストに追加

ab.sort(key=lambda ab: (-ab[0], ab[1]))

ans = ""
for i in ab:
    print(i[1]+1 , end=" ")

