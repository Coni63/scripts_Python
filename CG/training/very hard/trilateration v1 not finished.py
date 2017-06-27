import sys
import math

class grid():
    def __init__(self, la_map):
        self.grille = la_map
    
    def show(self):
        for each_line in self.grille:
            print(each_line, file=sys.stderr)
            
    def update_map(self, frontiere, direction, distance):
        for y in range(h):
            for x in range(w):
                if (direction=="UP" and distance == "WARMER") or (direction=="DOWN" and distance == "COLDER"):
                    if y < frontiere[0]*x+frontiere[1]:
                        self.grille[y][x]=1
                elif (direction =="DOWN" and distance == "WARMER") or (direction=="UP" and distance == "COLDER"):
                    if y > frontiere[0]*x+frontiere[1]:
                        self.grille[y][x]=1
            
class aDallas():
    def __init__(self, X0, Y0):
        self.position = (X0, Y0)
        self.previous_position = (-1,-1)
        self.distance = "UNKNOWN"
        
    def move(self, new_x, new_y):
        self.previous_position = self.position
        self.position = (new_x, new_y)
        print(str(new_x), str(new_y))
    
    def update_sensor(self, result):
        self.distance = result
        self.shift = (self.position[0]-self.previous_position[0], self.position[1]-self.previous_position[1])
        self.meditrice_normal = (-self.shift[1], self.shift[0])
        self.intersection_point = ((self.position[0]+self.previous_position[0])/2, (self.position[1]+self.previous_position[1])/2)
        self.mediatrice = (self.meditrice_normal[1]/self.meditrice_normal[0], self.intersection_point[1]-self.intersection_point[0]*self.meditrice_normal[1]/self.meditrice_normal[0])
        if self.shift[1] < 0:
            self.direction = "UP"
        elif self.shift[1] > 0:
            self.direction = "DOWN"
        else:
            if self.shift[0] < 0:
                self.direction = "LEFT"
            elif self.shift[0] > 0:
                self.direction = "RIGHT"
        print("Batman moves", self.direction,"by", self.shift, file=sys.stderr)
        print("La mediatrice est", self.mediatrice, file=sys.stderr)
        #self.shift = movement done at this step
        #self.meditrice_normal = vecteur directeur de la droite d'intersection
        #self.intersection point = point de la mediatrice
        #self.mediatrice = coef directeur et ordonnée a l'origine de la mediatrice () attention y est inversé (y+ vers le bas)

    def first_move(self):
        self.move((w-1)-self.position[0], (h-1)-self.position[1])
    
    def next_move(self, carte):
        max_dist = 0
        position = (0,0)
        for y in range(h):
            for x in range(w):
                if carte[y][x]==0:
                    dist = math.sqrt((self.position[0]-x)**2+(self.position[1]-y)**2)
                    print(dist, file=sys.stderr)
                    if dist > max_dist:
                        max_dist = dist
                        position = (x,y)
                        print(position, file=sys.stderr)
        self.move(position[0], position[1])
                    
        
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
carte = [[0 for x in range(w)] for x in range(h)] 
tower = grid(carte)
tower.show()

n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
batman = aDallas(x0, y0)
batman.first_move()

# game loop
while True:
    bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
    batman.update_sensor(bomb_dir)
    tower.update_map(batman.mediatrice, batman.direction, batman.distance)
    tower.show()
    batman.next_move(tower.grille)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

