import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

table=[]
min = 1000
n = int(input())

for i in range(n):
    pi = int(input())
    table.append(pi)
    
    
table=sorted(table)

for j in range(n-1):
    if math.fabs(table[j+1]-table[j])<min:
        min = int(math.fabs(table[j+1]-table[j]))
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(min)