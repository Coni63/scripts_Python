import sys
import math
import re
import time

morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
         "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
         "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.."}
dico = {}

l = input()
print(l, file=sys.stderr)

s = time.time()

n = int(input())
for i in range(n):
    w = input()
    w = w.upper()
    conv = ""
    for each in w:
        conv += morse[each]
    dico[w] = conv

print(dico, file=sys.stderr)

print(time.time() - s, file=sys.stderr)

count = 0
t = l[:]
r = None
while r != "":
    r = ""
    while True:
        for key, code in dico.items():
            if code == t[:len(code)]:
                t = t[len(code):]
                r += key
                del dico[key]
                break  # for
        if len(t) == 0:
            count += 1
            break
    print(r, file=sys.stderr)
print(count)

# To debug: print("Debug messages...", file=sys.stderr)