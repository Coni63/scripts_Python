import sys
import math
import re

morse = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--.."} 
dico = {}

l = input()
print(l, file=sys.stderr)  

n = int(input())
for i in range(n):
    w = input()
    w = w.upper()
    conv = ""
    for each in w:
        conv += morse[each]
    dico[w] = conv
print(dico, file=sys.stderr)
    
count = 0
for each in dico.keys():
    if dico[each] == l:
        count +=1

print(count)

# To debug: print("Debug messages...", file=sys.stderr)