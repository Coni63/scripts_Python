import sys
import math
import re

message = input()
print("message : ", message, file=sys.stderr)

binary_code = "".join(format(ord(x), 'b').zfill(7) for x in message)
print("code : ", binary_code, file=sys.stderr)

splitted_code = filter(None, re.split(r"(0+)(1+)", binary_code)) #do not print, else generator disappear

result =""
for each in splitted_code:
    if each.count("1") > 0:
        result +=" ".join(["0", "0"*each.count("1")]) + " "
    else:
        result +=" ".join(["00", "0"*each.count("0")]) + " "

print(result.strip())     
        
# Write an action using print
# To debug: print(mess, file=sys.stderr)


//////////////////////////////////////////////////////////////

import sys
import math
from itertools import groupby

message = input()
print("message : ", message, file=sys.stderr)

binary_code = "".join(format(ord(x), 'b').zfill(7) for x in message)
print("code : ", binary_code, file=sys.stderr)

res = []

for k, g in groupby(binary_code):
    nb = len(list(g))
    if k == "0":
        res.append("00")
        res.append("0" * nb)
    else:
        res.append("0")
        res.append("0" * nb)   

print(" ".join(res).strip())     
        
# To debug: print(mess, file=sys.stderr)