import sys
import math

reverse = {"LEFT":"RIGHT", "RIGHT":"LEFT", "UP":"DOWN", "DOWN":"UP"}
change_dir = {"LEFT":"DOWN", "RIGHT":"UP", "UP":"LEFT", "DOWN":"RIGHT"}
choice = {"UP":["DOWN","RIGHT","LEFT"],"DOWN":["RIGHT","LEFT","UP"],"RIGHT":["DOWN","LEFT","UP"],"LEFT":["DOWN","RIGHT","UP"]}

UNKNOWN = '?'
PART_OF_PATH = '.'
TRIED = 'o'
OBSTACLE = '#'
DEAD_END = '-'
START = 'T'
END = 'C' 

class new_carte():
    def __init__(self, la_map):
        self.maze = la_map
        self.start = []
        self.end = []
    
    def merge(self, new):
        for y in range(r):
            #self.status[y]={}
            for x in range(c):
                if self.maze[y][x] == UNKNOWN and new[y][x] != UNKNOWN:
                    self.maze[y] = self.maze[y][:x] + new[y][x] + self.maze[y][x+1:]
                if new[y][x] == END and self.end == []:
                    self.end = [y,x]
                #if self.maze[y][x] == "X":
                #    self.maze[y] = self.maze[y][:x] + new[y][x] + self.maze[y][x+1:]
                #if self.maze[y][x] == ".":
                #    self.status[y][x]=PART_OF_PATH
                #elif self.maze[y][x] == "#":
                #    self.status[y][x]=OBSTACLE
                #elif self.maze[y][x] == "X":
                #    self.status[y][x]=TRIED
                #elif self.maze[y][x] == "$":
                #    self.status[y][x]=DEAD_END
                
    def show(self):
        for y in range(r):
            print(self.maze[y], file=sys.stderr)
    
class aDallas():
    def __init__(self):
        self.path = [] #en y,x
        self.posi = [] #en y,x
        self.retour = False
        self.direction = None
                    
    def init_direction(self):
        if self.look("LEFT") != OBSTACLE:
			self.direction = "LEFT"
		elif self.look("RIGHT") != OBSTACLE:
			self.direction = "RIGHT"
		elif self.look("UP") != OBSTACLE:
			self.direction = "UP"
		else:
			self.direction = "DOWN"
    
    def look(self, direction):
		global full_map
        if direction == "UP":
            return full_map.maze[self.posi[0]-1][self.posi[1]]
        elif direction == "DOWN":
            return full_map.maze[self.posi[0]+1][self.posi[1]]
        elif direction == "RIGHT":
            return full_map.maze[self.posi[0]][self.posi[1]+1]
        elif direction == "LEFT":
            return full_map.maze[self.posi[0]][self.posi[1]-1] 
            
    def dropBreadCrumb(self):
		global full_map
        x = self.posi[1]
        y = self.posi[0]
        if full_map.maze[y][x] == PART_OF_PATH:
            full_map.maze[y] = full_map.maze[y][:x] + TRIED + full_map.maze[y][x+1:]
        elif full_map.maze[y][x] == TRIED:
            full_map.maze[y] = full_map.maze[y][:x] + OBSTACLE + full_map.maze[y][x+1:]
    
    def find_path(self):
		global full_map
        if self.retour == False: #si on n'est pas sur la route du retour
            if self.posi == carte.end: #si on atteint la console
                self.retour = True
                return reverse[self.path.pop(-1)]
            else: #si on n'est pas a la console
                flag = False
                prev_dir = self.direction
                while flag == False:
                    if self.look(self.direction) == OBSTACLE:
                        new_dir = change_dir[self.direction]
                        if new_dir == reverse[prev_dir]:
                            new_dir = change_dir[new_dir]
                        self.direction=new_dir
                    else:
                        flag = True
                
                self.path.append(self.direction)
                return self.direction   
        else:
            return reverse[self.path.pop(-1)]
            
# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]

kirk = aDallas()
step=0
# game loop
while True and step < 100:
    step+=1
    new_map = [] 
    # kr: row where Kirk is located.
    # kc: column where Kirk is located.
    kr, kc = [int(i) for i in input().split()]
    kirk.posi=[kr, kc]
    
    for i in range(r):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        new_map.append(row)
    
    if "full_map" not in globals():
        full_map = new_carte(new_map)
        full_map.start = [kr, kc]
        kirk.init_direction(full_map)
    else:
        full_map.merge(new_map)
    
    direction = kirk.find_path(full_map)
    print(direction)
    kirk.dropBreadCrumb(full_map)
    full_map.show()
    
    # To debug: print("Debug messages...", file=sys.stderr)