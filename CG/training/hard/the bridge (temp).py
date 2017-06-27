import sys
import math
import time
import copy
import itertools

class Branch():
    def __init__(self, path, elem, score = 0):
        self.path = path
        self.state = elem
        self.score = score

class Tree():
    def __init__(self):
        self.depth = 3
        self.choices = ["SPEED", "SLOW", "JUMP", "WAIT", "UP", "DOWN"]
        self.tree = []
        self.previous_tree = []
        
    def create_child(self, branche):
        for each in self.choices:
            temp_team = new_instance(branche.state)
            score = temp_team.play(each) + branche.score
            print("Testing ..." , branche.path + [each] , "- score :" , score , file=sys.stderr)
            temp_path = branche.path + [each]
            if score >= 0:
                self.tree.append(Branch(temp_path, temp_team, score))
            
    def populate(self):
        for _ in range(1, self.depth):
            self.previous_tree = self.tree
            self.tree = []
            for each_branch in self.previous_tree:
                self.create_child(each_branch)
            
    def show(self):
        for each in self.tree:
            attrs = vars(each)
            print(', '.join("%s: %s" % item for item in attrs.items()), file = sys.stderr)        
    
    def get_max(self):
        top_score = -1
        current_leader = self.tree[0]
        for each in self.tree:
            if each.score > top_score:
                current_leader = each
                top_score = each.score
        return current_leader.path
    
def new_instance(classe):
    return copy.deepcopy(classe)

class Team():
    def __init__(self, moto_start, moto_mini):
        self.members = []
        self.minimum = moto_mini
        self.lines = [0, 0, 0, 0]
        self.x = 0
        self.speed = 0
        
    def remaining_bike(self):
        i = 0
        for each in self.members:
            if each.alive == 1:
                i +=1 
        return i
    
    def reset_lines(self):
        self.lines = [0, 0, 0, 0]
    
    def up(self):
        count = 0
        for i in range(1, 4):
            if self.lines[i-1] == 0 and self.lines[i] != 0:
                self.lines[i-1] = self.lines[i]
                self.lines[i] = 0
                self.lines[i-1].line -= 1
                
                moto = self.lines[i-1]
                sector_top = road[i-1][self.x:self.x+self.speed]
                sector_bot = road[i][self.x:self.x+self.speed-1]
                if "#" in sector_top or "#" in sector_bot:
                    moto.alive = 0
                if moto.alive == 1:
                    count += 1
        self.x += self.speed
        if count == 0 or self.speed == 0:
            return -100
        else:
            return 3*count
    
    def down(self):
        count = 0
        for i in reversed(range(0, 3)):
            if self.lines[i+1] == 0 and self.lines[i] != 0:
                self.lines[i+1] = self.lines[i]
                self.lines[i] = 0
                self.lines[i+1].line -= 1
            
                moto = self.lines[i+1]
                sector_top = road[i+1][self.x:self.x+self.speed]
                sector_bot = road[i][self.x:self.x+self.speed-1]
                if "0" in sector_top or "0" in sector_bot:
                    moto.alive = 0
                if moto.alive == 1:
                    count += 1
        self.x += self.speed
        if count == 0 or self.speed == 0:
            return -100
        else:
            return 3*count
    
    def speed_up(self):
        count = 0
        self.speed += 1
        #if self.speed > biggest_hole+1:
        #    return -100
        #else:
        for moto in self.members:
            if "0" in road[moto.line][self.x:self.x+self.speed]:
                moto.alive = 0
        self.x += self.speed
        return 50
            
    def slow_down(self):
        count = 0
        self.speed -= 1
        if self.speed < biggest_hole+1:
            return -100
        else:
            for moto in self.members:
                if "0" in road[moto.line][self.x:self.x+self.speed]:
                    moto.alive = 0
            self.x += self.speed    
            return 0
    
    def jump(self):
        score = 0
        if self.speed == 0:
            return -100
        else:
            for moto in self.members: 
                #print(road[moto.line][self.x+1:self.x+self.speed+1], file=sys.stderr)
                if "0" in road[moto.line][self.x:self.x+self.speed]:
                    score += 100
                if road[moto.line][self.x+self.speed] == "0" or road[moto.line][self.x] == "0":
                    moto.alive = 0
            self.x += self.speed
        return score
    
    def wait(self):
        if self.speed == 0:
            return -100
        else:  
            for moto in self.members: 
                if "0" in road[moto.line][self.x:self.x+self.speed]:
                    moto.alive = 0
            self.x += self.speed
        return 1
        
    def play(self, commande):
        if commande == "SPEED":
            score = self.speed_up()
        elif commande == "SLOW":
            score = self.slow_down()
        elif commande == "JUMP":
            score = self.jump()
        elif commande == "WAIT":
            score = self.wait()
        elif commande == "UP":
            score = self.up()
        elif commande == "DOWN":
            score = self.down()
        #print(team.remaining_bike(), file=sys.stderr)
        if self.remaining_bike() < self.minimum:
            score = 100
        return score
    
    def show(self):
        print("x: %s: speed: %s" % (self.x, self.speed), file = sys.stderr)
        for item in self.members:
            item.show()
        print(self.lines, file = sys.stderr)
            
class Bike():
    def __init__(self):
        self.line = 0
        self.alive = 1
        team.members.append(self)
        
    def update(self, y, a):
        self.line = y
        self.alive = a
        team.lines[y] = self
        
    def show(self):
        attrs = vars(self)
        print( self, ', '.join("%s: %s" % item for item in attrs.items()), file = sys.stderr)
              
m = int(input())  # the amount of motorbikes to control
v = int(input())  # the minimum amount of motorbikes that must survive

loop = 0
road = []
time_history = []

biggest_hole = 0
for _ in range(4):
    path = input() + "......................................................................................................."
    road.append(path)
    for k, g in itertools.groupby(path):
        if k == "0":
            size = len(list(g))
            biggest_hole = max(biggest_hole, size)
    print(path, file = sys.stderr)

#print("", file = sys.stderr)

team = Team(m, v)
for _ in range(m):
    Bike()

# game loop
while True:
    start = time.time()
    
    team.reset_lines()
    
    team.speed = int(input())  # the motorbikes' speed
    for i in range(m):
        x, y, a = [int(j) for j in input().split()]
        team.x = x
        team.members[i].update(y, a)
    
    #team.show()
    
    arbre = Tree()
    root = Branch([], team)
    arbre.create_child(root)
    arbre.populate()
    track = arbre.get_max()
    print(track[0])
    
    duration = (time.time()-start)*1000
    if loop > 0:
        time_history.append(duration)
        print("", file = sys.stderr)
        print("time {:06.2f} ms (min {:06.2f}ms - max {:06.2f}ms - avg {:06.2f}ms)".format(duration, min(time_history), max(time_history), sum(time_history)/len(time_history) ), file=sys.stderr)
    else:
        print("", file = sys.stderr)
        print("time {:06.2f} ms".format(duration), file=sys.stderr)
    loop+=1