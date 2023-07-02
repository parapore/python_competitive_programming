import math
from fractions import Fraction

a, b = map(Fraction, input().split())
ans = math.floor(a*b)
print(ans)