import sys
import math


class Map:
    def __init__(self):
        self.width = 23
        self.height = 21
        self.carte = [[0]*self.width]*self.height
        self.mine_list = []
        self.barrel_list = []

    def show(self):
        for i in range(self.height):
            print(self.carte[i], file=sys.stderr)

    def add_barrel(self, x, y):
        self.carte[y][x] = "B"
        self.barrel_list.append((x, y))

    def add_mine(self, x, y):
        self.carte[y][x] = "M"
        self.mine_list.append((x, y))


class Chips:
    my_chips = {}
    instances = {}
    def __init__(self, X, Y, ID, A1, A2, A3, A4):
        self.x = X
        self.y = Y
        self.ID = ID
        self.type = "SHIP"
        self.orientation = A1
        self.speed = A2
        self.stock = A3
        self.team = A4
        if self.team == 1:
            self.my_chips[self.ID] = self
        self.instances[self.ID] = self
        self.distance = {}

    def __repr__(self):
        return "Chip {} - stock {} - position ( {} , {} ) - speed {} ".format(self.ID, self.stock, self.x, self.y, self.speed)

    def update(self, X, Y, A1, A2, A3, A4):
        self.x = X
        self.y = Y
        self.orientation = A1
        self.speed = A2
        self.stock = A3
        self.team = A4
        self.distance = {}

    def set_distances(self):
        for barrel in barrels.instances:
            print(barrel, file=sys.stderr)
            self.distance[barrel] = ((self.x-barrel.x)**2 + (self.y-barrel.y)**2)**0.5

    def go_to_closest(self):
        mini=1000
        target = None
        for b, d in self.distance.items():
            if d < mini:
                target = b
                mini = d

        if target != None:
            print("MOVE {} {}".format(target.x, target.y))
        else:
            print("MOVE {} {}".format(11, 10))


class barrels:
    instances = []
    def __init__(self, X, Y, ID, A1):
        self.x = X
        self.y = Y
        self.ID = ID
        self.type = "SHIP"
        self.stock = A1
        self.instances.append(self)

    def __repr__(self):
        return "Barrel {} - {} L - Pos : ( {} , {} )".format(self.ID, self.stock, self.x, self.y)

grid = Map()
grid.show()

# game loop
while True:
    my_ship_count = int(input())  # the number of remaining ships
    entity_count = int(input())  # the number of entities (e.g. ships, mines or cannonballs)
    barrels.instances = []
    for i in range(entity_count):
        entity_id, entity_type, x, y, arg_1, arg_2, arg_3, arg_4 = input().split()
        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)
        #print(entity_type, file=sys.stderr)
        if entity_type == "SHIP":
            if entity_id in Chips.instances.keys():
                Chips.instances[entity_id].update(x, y, arg_1, arg_2, arg_3, arg_4)
            else:
                t = Chips(x, y, entity_id, arg_1, arg_2, arg_3, arg_4)
                #print(t, "created", file=sys.stderr)
        elif entity_type == "BARREL":
            t = barrels(x, y, entity_id, arg_1)
            #print(t, "created", file=sys.stderr)

    print(barrels.instances, file=sys.stderr)

    for ID, chip in Chips.my_chips.items():
        print(chip, file=sys.stderr)
        print(chip.distance, file=sys.stderr)
        chip.set_distances()
        chip.go_to_closest()
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        # Any valid action, such as "WAIT" or "MOVE x y"
