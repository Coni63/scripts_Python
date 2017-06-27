import sys
import math

l, c, n = [int(i) for i in input().split()]

file = []
gain = 0
index = 0
run = 0
start = 0
listing = {}

for i in range(n):
    pi = int(input())
    file.append(pi)

print(file, file=sys.stderr)
  
taille_file = sum(file) 

if taille_file > l:
    for i in range(n): #for each start
        nb_pers = 0
        index = 0
        while nb_pers + file[i+index] <= l:
            nb_pers += file[i+index]
            index += 1
            if i+index == n:
                index = -i 
        listing[i] = [nb_pers, i+index]
    print(listing, file=sys.stderr)
    
    for i in range(c):
        gain += listing[start][0]
        start = listing[start][1]   
else:
    gain = c * taille_file
            
# To debug: print("Debug messages...", file=sys.stderr)
print(gain)
