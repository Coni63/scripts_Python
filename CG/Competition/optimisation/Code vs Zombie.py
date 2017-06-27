import sys
import math

class Human:
    instances = {}
    def __init__(self, X, Y, ID):
        self.x = X
        self.y = Y
        self.id = ID
        self.instances[self.id] = self
        self.distances = {}
        
    def update(self, X, Y):
        self.x = X
        self.y = Y
        
    def set_distances(self):
        for zombie in Zombie.instances.values():
            d = math.sqrt((self.x - zombie.x)**2 + (self.y - zombie.y)**2)
            self.distances[zombie] = d
            
    def goto(self, target):
        print("{} {}".format(target.x, target.y))

class Zombie:
    instances = {}
    def __init__(self, ID, X, Y, next_X, next_Y):
        self.x = X
        self.y = Y
        self.id = ID
        self.nx = next_X
        self.ny = next_Y
        self.instances[self.id] = self
        
    def update(self, X, Y, next_X, next_Y):
        self.x = X
        self.y = Y
        self.nx = next_X
        self.ny = next_Y

    def __repr__(self):
        return "Z{}".format(self.id)

while True:
    x, y = [int(i) for i in input().split()]
    me = Human(x, y, 999)
    
    Human.instances = {}
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        Human(human_x, human_y, human_id)
        #if human_id in Human.instances.keys():
        #    Human.instances[human_id].update(human_x, human_y)
        #else:
        #    Human(human_x, human_y, human_id)
        
        
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        if zombie_id in Zombie.instances.keys():
            Zombie.instances[zombie_id].update(zombie_x, zombie_y, zombie_xnext, zombie_ynext)
        else:
            Zombie(zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext)
    
    if human_count == 1:
        me.goto(list(Human.instances.values())[0])
    else:
        closest = 30000
        need_protect = None
        for each in Human.instances.values():
            each.set_distances()
            #if can be saved ...
            for key, dist in each.distances.items():
                if dist < closest:
                    closest = dist
                    need_protect = each
            print(each.distances, file=sys.stderr)
        me.goto(need_protect) 
    