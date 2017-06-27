import sys
import math

type_block = {  0:{"BLOCK":"BLOCK"}, 
                1:{"RIGHT":"BOTTOM", "LEFT":"BOTTOM", "TOP":"BOTTOM"},
                2:{"RIGHT":"LEFT", "LEFT":"RIGHT"}, 
                3:{"TOP":"BOTTOM"}, 
                4:{"TOP":"LEFT", "RIGHT":"BOTTOM"}, 
                5:{"TOP":"RIGHT", "LEFT":"BOTTOM"}, 
                6:{"RIGHT":"LEFT", "LEFT":"RIGHT"}, 
                7:{"RIGHT":"BOTTOM", "TOP":"BOTTOM"}, 
                8:{"RIGHT":"BOTTOM", "LEFT":"BOTTOM"}, 
                9:{"LEFT":"BOTTOM", "TOP":"BOTTOM"}, 
                10:{"TOP":"LEFT"}, 
                11:{"TOP":"RIGHT"}, 
                12:{"RIGHT":"BOTTOM"}, 
                13:{"LEFT":"BOTTOM"}
            }

rotate = { "RIGHT" : {2:3, 3:2, 4:5, 5:4, 6:7, 7:8, 8:9, 9:6, 10:11, 11:12, 12:13, 13:10}, 
            "LEFT" : {2:3, 3:2, 4:5, 5:4, 6:9, 9:8, 8:7, 7:6, 10:13, 13:12, 12:11, 11:10} }

invert = {"RIGHT":"LEFT", "LEFT":"RIGHT", "BOTTOM":"TOP"}

arr = []

def check_orientation(direction, blockID, rotation):
    global xi, w
    if xi == 0 or xi == w:
        out = ["BOTTOM"]
    else:
        out = ["BOTTOM","LEFT","RIGHT"]
    
    if rotation != "NONE":
        new_blockID = rotate[rotation][abs(blockID)]
    else:
        new_blockID = blockID
    
    if direction not in type_block[new_blockID].keys() or type_block[new_blockID][direction] not in out: #si on ne peut pas rentrer par ce coté ou si ca sort au top
        return False
    else:
        return True
 
def rotate_block(pos, sens):
    arr[pos[1]][pos[0]] = -rotate[sens][abs(int(arr[pos[1]][pos[0]]))]
    print(pos[0], pos[1], sens)

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()  # each line represents a line in the grid and contains W integers T. The absolute value of T specifies the type of the room. If T is negative, the room cannot be rotated.
    arr.append(line.split(" "))
    print(line, file=sys.stderr)
ex = int(input())  # the coordinate along the X axis of the exit.

# game loop
while True:
    xi, yi, side = input().split()
    xi = int(xi)
    yi = int(yi)
    r = int(input())  # the number of rocks currently in the grid.
    for i in range(r):
        xr, yr, posr = input().split()
        xr = int(xr)
        yr = int(yr)
    
    # on recup l'id de notre block et le coté par lequel on sort
    block = int(arr[yi][xi])
    out_direction = type_block[abs(block)][side]
    
    #selon d'ou on sort, on calcul notre position suivant
    if out_direction == "BOTTOM":
        next_pos = [xi, yi+1]
    elif out_direction == "LEFT":
        next_pos = [xi-1, yi]
    elif out_direction == "RIGHT":
        next_pos = [xi+1, yi]
    
    #on connait donc le block suivant et le sens d'arrivé
    in_direction = invert[out_direction]
    next_block = int(arr[next_pos[1]][next_pos[0]])
    
    
    if next_block > 0:
        if check_orientation(in_direction, next_block, "NONE"): #si on peut sortir sans tourner
            print("WAIT")
        elif check_orientation(in_direction, next_block,"RIGHT"): #sinon on verifie en tournant a droite
            rotate_block(next_pos, "RIGHT")
        elif check_orientation(in_direction, next_block, "LEFT"): #ou a gauche
            rotate_block(next_pos, "LEFT")
    else:
        print("WAIT")            
    

    # To debug: print("Debug messages...", file=sys.stderr)
