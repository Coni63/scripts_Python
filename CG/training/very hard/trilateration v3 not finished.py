import sys
import math
import time
                    
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
            #si on monte et qu'on est plus proche, on garde la partie haute
            #si on descend et qu'on est plus loin, on garde la partie haute
            if (self.shift[1]>0 and result == "WARMER") or (self.shift[1]<0 and result == "COLDER"): 
                min_y = math.floor((self.position[1]+self.previous_position[1])/2)
            elif (self.shift[1]<0 and result == "WARMER") or (self.shift[1]>0 and result == "COLDER"):
                max_y = math.ceil((self.position[1]+self.previous_position[1])/2)
            elif result == "SAME":
                if (self.position[1]-self.previous_position[1])%2 == 0:
                    max_y = max(math.floor((self.position[1]+self.previous_position[1])/2), math.ceil((self.position[1]+self.previous_position[1])/2))
                    min_y = min(math.floor((self.position[1]+self.previous_position[1])/2), math.ceil((self.position[1]+self.previous_position[1])/2))
                else:
                    max_y = (self.position[1]+self.previous_position[1])/2
                    min_y = max_y
        else:
            #si on va a gauche et qu'on est plus proche, on garde la partie gauche
            #si on va a droite et qu'on est plus loin, on garde la partie gauche
            #si on va a droite et qu'on est plus proche, on garde la partie droite
            #si on va a gauche et qu'on est plus loin, on garde la partie droite
            if (self.shift[0]<0 and result == "WARMER") or (self.shift[0]>0 and result == "COLDER"): 
                max_x = math.ceil((self.position[0]+self.previous_position[0])/2)
            elif (self.shift[0]>0 and result == "WARMER") or (self.shift[0]<0 and result == "COLDER"):
                min_x = math.floor((self.position[0]+self.previous_position[0])/2)
            elif result == "SAME":
                if (self.position[0]-self.previous_position[0])%2 == 0:
                    max_y = max(math.floor((self.position[0]+self.previous_position[0])/2), math.ceil((self.position[0]+self.previous_position[0])/2))
                    min_y = min(math.floor((self.position[0]+self.previous_position[0])/2), math.ceil((self.position[0]+self.previous_position[0])/2))
                else:
                    max_y = (self.position[0]+self.previous_position[0])/2
                    min_y = max_y
            
    def invert_direction(self):
        if abs(max_y-min_y) > (max_x-min_x):
            self.direction = "HORIZONTAL"
        else:
            self.direction = "VERTICAL"
        #if self.direction == "HORIZONTAL" and (max_x-min_x)>1:
        #    self.direction = "VERTICAL"
        #elif self.direction == "VERTICAL" and (max_y-min_y)>1:
        #    self.direction = "HORIZONTAL"
    
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
          
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
min_x, max_x, min_y, max_y = 0, w-1, 0, h-1
print(w,h, file=sys.stderr)
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
batman = aDallas(x0, y0)

# game loop
while True:
    bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
    print(bomb_dir, file=sys.stderr)
    
    if bomb_dir == "UNKNOWN":
        batman.first_move()
    else:
        start_time_round = time.time() 
        print(batman.direction, file=sys.stderr)
        batman.update_sensor(bomb_dir)
        print(min_x, max_x, file=sys.stderr)
        print(min_y, max_y, file=sys.stderr)
        batman.split()

        interval = time.time() - start_time_round     
        print("Round time : ", interval, file=sys.stderr)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

