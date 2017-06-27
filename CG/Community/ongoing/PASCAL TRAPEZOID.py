import sys
import math

def next_line(starting_line):
    output = []
    for i in range(len(starting_line)+1):
        if i == 0:
            output.append(starting_line[i])
        elif i == len(starting_line):
            output.append(starting_line[i-1])
        else:
            first = str(starting_line[i-1])
            second = str(starting_line[i])
            if first.isnumeric() and second.isnumeric():
                out = int(first) + int(second)
            else:
                out = first + second
            output.append(out)
    return output


start_lvl, end_lvl, elem_number = [int(i) for i in input().split()]
start_line = input().split()

result = start_line

for _ in range(end_lvl-1):
    result = next_line(result)
    
#print(result, file=sys.stderr)
print(result[elem_number-1])


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


