import sys
import math

visited = {}

def pos_str(x,y):
    return str(x) + "-" + str(y)

def expand(x,y, old_x=None, old_y=None):
    print("expand on " + pos_str(x,y), file=sys.stderr)
    count = 0
    if mapping[y][x] == "O":
        count += 1
        if x+1 != old_x and x+1 <= l-1 and pos_str(x+1,y) not in visited.keys():
            visited[pos_str(x+1,y)]=1
            count += expand(x+1, y, x, y)
        if x-1 != old_x and x-1 >= 0 and pos_str(x-1,y) not in visited.keys():  
            visited[pos_str(x-1,y)]=1
            count += expand(x-1, y, x, y)
        if y+1 != old_y and y+1 <= h-1 and pos_str(x,y+1) not in visited.keys():
            visited[pos_str(x,y+1)]=1
            count += expand(x, y+1, x, y)
        if y-1 != old_y and y-1 >= 0 and pos_str(x,y-1) not in visited.keys():
            visited[pos_str(x,y-1)]=1
            count += expand(x, y-1, x, y)
    return count

mapping = []

l = int(input())
h = int(input())

water = 0
for i in range(h):
    row = input()
    mapping.append(row)
    for each_char in row:
        if each_char == "O":
            water +=1
            
print(water, file=sys.stderr)

n = int(input())
for i in range(n):
    if 1000*water/(l*h)<500 :
        visited = {}
        x, y = [int(j) for j in input().split()]
        visited[pos_str(x,y)]=1
        n = expand(x,y)
        print(n)
    else:
        print(water)
        
            
                  
        
            


    # To debug: print("Debug messages...", file=sys.stderr)

    