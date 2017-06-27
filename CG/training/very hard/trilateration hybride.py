import sys
import math
import time
from collections import defaultdict

class grid():
    def __init__(self, la_map):
        self.grille = la_map
        self.width = len(la_map[0])
        self.height = len(la_map)
    
    def show(self):
        for each_line in self.grille:
            print(each_line, file=sys.stderr)
            
    def update_map(self, pos1, pos2, dist):
        for y in range(self.height):
            for x in range(self.width):
                if self.grille[y][x] == 0:
                    if (x,y) in memo_dist.keys():
                        dist1 = memo_dist[(x,y)]
                    else:    
                        dist1 = math.sqrt((pos1[0]-x)**2+(pos1[1]-y)**2) #distance from previous point 
                    dist2 = math.sqrt((pos2[0]-x)**2+(pos2[1]-y)**2) #distance from latest position
                    memo_dist[(x,y)]=dist2
                    if dist == "COLDER" and dist1 > dist2: #si on s'eloigne et que la distance d'origine est plus grande que la nouvelle
                        self.grille[y][x]=1
                        del memo_dist[(x,y)]
                    elif dist == "WARMER" and dist2 > dist1:
                        self.grille[y][x]=1
                        del memo_dist[(x,y)]
                    elif dist == "SAME" and dist1 != dist2:
                        self.grille[y][x]=1
                        del memo_dist[(x,y)]
                        
    def set_offset(self, off_x, off_y):
        self.offset_x = off_x
        self.offset_y = off_y
                
class aDallas():
    def __init__(self, X0, Y0):
        self.position = (X0, Y0)
        self.previous_position = (-1,-1)
        self.distance = "UNKNOWN"
        
    def move(self, new_x, new_y):
        self.previous_position = self.position
        self.position = (new_x, new_y)
        self.shift = (self.position[0]-self.previous_position[0], self.position[1]-self.previous_position[1])
        print(str(new_x), str(new_y))
    
    def update_sensor(self, result):
        global min_x, max_x, min_y, max_y
        self.distance = result
        if self.direction == "HORIZONTAL":
            #si on descend et qu'on est plus proche, on garde la partie basse
            #si on monte et qu'on est plus loin, on garde la partie basse
            if (self.shift[1]>0 and result == "WARMER") or (self.shift[1]<0 and result == "COLDER"): 
                min_y = math.floor((self.position[1]+self.previous_position[1])/2)
            #si on monte et qu'on est plus proche, on garde la partie haute
            #si on descend et qu'on est plus loin, on garde la partie haute
            elif (self.shift[1]<0 and result == "WARMER") or (self.shift[1]>0 and result == "COLDER"):
                max_y = math.ceil((self.position[1]+self.previous_position[1])/2)
            #si on est a la meme distance, on n'a qu'une ligne dispo
            elif result == "SAME":
                max_y = int((self.position[1]+self.previous_position[1])/2)
                min_y = max_y
        else:
            #si on va a gauche et qu'on est plus proche, on garde la partie gauche
            #si on va a droite et qu'on est plus loin, on garde la partie gauche
            if (self.shift[0]<0 and result == "WARMER") or (self.shift[0]>0 and result == "COLDER"): 
                max_x = math.ceil((self.position[0]+self.previous_position[0])/2)
            #si on va a droite et qu'on est plus proche, on garde la partie droite
            #si on va a gauche et qu'on est plus loin, on garde la partie droite      
            elif (self.shift[0]>0 and result == "WARMER") or (self.shift[0]<0 and result == "COLDER"):
                min_x = math.floor((self.position[0]+self.previous_position[0])/2)
            #si on est a la meme distance, on n'a qu'une colonne dispo
            elif result == "SAME":
                max_y = int((self.position[0]+self.previous_position[0])/2)
                min_y = max_y
            
    def invert_direction(self):
        if (max_x-min_x)==0: #si on a une seule colonne
            self.direction = "HORIZONTAL" #on split horizontalement
        elif (max_y-min_y)==0: #si on a une seule ligne
            self.direction = "VERTICAL" #on split verticalement
        else: #sinon, on a un rectangle
            if abs(max_y-min_y) > (max_x-min_x): #on split par le plus grand coté
                self.direction = "HORIZONTAL"
            else:
                self.direction = "VERTICAL"
    
    def first_move(self):
        if h > w:
            self.direction = "HORIZONTAL"
            self.move(self.position[0], h-self.position[1])
        else:
            self.direction = "VERTICAL"
            self.move(w-self.position[0], self.position[1])
        
    def split(self):
        global w, h
        self.invert_direction()
        if self.direction == "VERTICAL":
            if abs(min_x-self.position[0]) > abs(max_x-self.position[0]):
                next_x = min_x
            else:
                next_x = max_x
            self.move(next_x, self.position[1])
        elif self.direction == "HORIZONTAL":
            if abs(min_y-self.position[1]) > abs(max_y-self.position[1]):
                next_y = min_y
            else:
                next_y = max_y
            self.move(self.position[0], next_y)
            
    def move_second(self, new_x, new_y):
        global tower
        tower.grille[new_y-tower.offset_y-1][new_x-tower.offset_x-1] = 1
        self.previous_position = self.position
        self.position = (new_x, new_y)
        print(str(new_x), str(new_y))
    
    def update_sensor_second(self, result):
        self.distance = result
    
    def next_move_second(self, carte):
        max_dist = 0
        position = (0,0)
        for y in range(carte.height):
            for x in range(carte.width):
                if carte.grille[y][x]==0:
                    dist = memo_dist[(x,y)]
                    if dist > max_dist:
                        max_dist = dist
                        position = (x,y)
        self.move_second(position[0]+carte.offset_x, position[1]+carte.offset_y)
          
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
min_x, max_x, min_y, max_y = 0, w-1, 0, h-1
print(w,h, file=sys.stderr)
memo_dist = defaultdict(list)    
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
batman = aDallas(x0, y0)
first_time = True
# game loop
while True:
    bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
    print(bomb_dir, file=sys.stderr)
    
    if bomb_dir == "UNKNOWN":
        batman.first_move()
    else:
        start_time_round = time.time() 
        print(batman.direction, file=sys.stderr)
        if abs(max_x-min_x)*abs(max_y-min_y) > 10000:
            batman.update_sensor(bomb_dir)
            print(min_x, max_x, file=sys.stderr)
            print(min_y, max_y, file=sys.stderr)
            batman.split()
        else:
            if first_time == True:
                carte = [[0 for x in range(abs(max_x-min_x))] for x in range(abs(max_y-min_y))] 
                tower = grid(carte)
                tower.set_offset(min_x, min_y)
                first_time = False
            batman.update_sensor_second(bomb_dir)
            tower.update_map(batman.previous_position, batman.position, batman.distance)
            #tower.show()
            batman.next_move_second(tower)
        interval = time.time() - start_time_round     
        print("Round time : ", interval, file=sys.stderr)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

