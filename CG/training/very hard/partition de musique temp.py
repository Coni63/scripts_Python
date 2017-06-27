import sys
import math
import numpy as np
import time
import itertools

#test = "CH CQ DQ CH EH CQ CQ AQ CH EQ DH CQ CQ DH CQ DQ CH CQ DQ EQ FQ AQ BQ CQ DQ EQ FQ GH CH CQ DQ CH EH CQ CQ AQ CH EQ DH CQ CQ DH CQ DQ CH CQ DQ EQ FQ AQ BQ CQ DQ EQ FQ GH CH CQ DQ CH EH CQ CQ AQ CH EQ DH CQ CQ DH CQ DQ CH CQ DQ EQ FQ AQ BQ CQ DQ EQ FQ GH"
#print(len(test.split(" ")), file=sys.stderr)
OFFSET_PARTITION = 10
LINE_THICKNESS = 4

start_time = time.time() 

w, h = [int(i) for i in input().split()]
print(w,h, file=sys.stderr)

image = input()
image_splitted = image.split(' ')

#generation d'un array de 0 (White) ou 1(Black) de w*h de long 
img_array = []
for index in range(int(len(image_splitted)/2)):
    if image_splitted[2*index] == "B":
        img_array += [1] * int(image_splitted[2*index+1])
    else:
        img_array += [0] * int(image_splitted[2*index+1])

#print("Pixel White : ", img_array.count(0), file=sys.stderr) 
#print("Pixel Black : ", img_array.count(1), file=sys.stderr)

#conversion en numpy matrix de w de large et h de haut avec uniquement des booleens (False = White, True = Black)
np_image = np.fromiter(img_array, dtype=np.bool).reshape(h, w) #

#suppression des parties blanches en amont et aval de la partition (10 pxl chaque coté)
for x in range(OFFSET_PARTITION):
    np_image = np.delete(np_image, 0, 0)
    np_image = np.delete(np_image, 0, -1)

#on redefini le w
w -= 2*OFFSET_PARTITION

# detection of lines
#print(np_image[:,0], file=sys.stderr)
test = [np.sum(np_image[:,x]) for x in range(w)]
start = []

for x in range(w-1):
    if test[x] <= 10*LINE_THICKNESS and test[x+1] > 10*LINE_THICKNESS:
        start.append(x)

print(len(start), file=sys.stderr)
    
    
"""
index_note = []
No_note = True
for x in range(column+1, w-column-1):
    new_col = []
    for y in range(empty_col[0]+1,empty_col[-1]+1):
        if np_image[y][x] == True:
            new_col.append(y)
            
    if new_col == empty_col:
        No_note = True
    elif No_note == True and new_col != empty_col:
        No_note = False
        index_note.append(x)
    else:
        continue
        
print("number of notes : ", len(index_note), file=sys.stderr)
"""
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("AQ DH")

print("Execution time : ", time.time() - start_time  , file=sys.stderr)