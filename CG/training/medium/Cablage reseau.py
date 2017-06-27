import sys
import math
from operator import itemgetter
import statistics

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

p_x = []
p_y = []

n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    p_x.append(x)
    p_y.append(y) 

#table = sorted(table, key=itemgetter(0))

dx = max(p_x)-min(p_x)
tot_y = sum(p_y)
avg_y = tot_y/n
med = statistics.median(p_y)

if avg_y>=0:
    avg_y1 = int(avg_y)
    avg_y2 = int(avg_y)+1
else:
    avg_y1 = int(avg_y)
    avg_y2 = int(avg_y)-1

l = 0
l1 = 0
l2 = 0
l3 = 0

for i in range(n):
    l1+=abs(p_y[i]-avg_y1)
    l2+=abs(p_y[i]-avg_y2)
    l3+=abs(p_y[i]-med)
          
l=min(l1, l2, l3) + dx
print(l)

# To debug: print("Debug messages...", file=sys.stderr)


