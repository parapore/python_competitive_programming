import re
s = input()

if re.fullmatch(r'^[A-Z][1-9][0-9]{5}[A-Z]$', s):
    print("Yes")
else:
    print("No")