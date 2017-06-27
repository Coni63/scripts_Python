import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, s = [int(i) for i in input().split()]
d = input()

arr = [x+1 for x in range(n)]
print(arr, file=sys.stderr)

current_index = s-1

while len(arr) >= 2:
    l = len(arr)
    if d == 'LEFT':
        next_index = (current_index + 1) % l
        arr.pop(next_index)
        current_index = next_index
    else:
        next_index = (current_index - 1 + l) % l
        next_pos = (current_index - 2 + l) % l
        arr.pop(next_index)
        current_index = next_pos
    print(arr, file=sys.stderr)

print(arr[0])
