import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, r = [int(i) for i in input().split()]

#l, r = 0, 10000
lucky = 0

gen = (str(i) for i in range(l, r+1))

"""
for i in gen:
    if ("6" in i and not "8" in i) or ("8" in i and not "6" in i):
        lucky += 1
"""

for number in gen:
    if (number.count("6") > 0) ^ (number.count("8") > 0):
        lucky += 1

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(lucky)
