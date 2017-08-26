import sys
import math
import random

class Gene:
    def __init__(self, init_genome = []):
        self.genome = init_genome
        self.score = 0
        if init_genome == []:
            self.generate()

    def generate(self):
        self.genome = [random.randint(0, z-1) for _ in range(d)]

    def mutate(self):
        pos = random.randint(0, d - 1)
        val = random.randint(0, z - 1)
        genome = self.genome[:]
        genome[pos] = val
        new_gene = Gene(genome)
        new_gene.evaluate()
        return new_gene

    def cross(self, other, position):
        a = self.genome[:]
        b = other.genome[:]
        new_a = a[:position] + b[position:]
        new_b = b[:position] + a[position:]
        new_gene_a = Gene(new_a)
        new_gene_a.evaluate()
        new_gene_b = Gene(new_b)
        new_gene_b.evaluate()
        print("new: \n", new_gene_a, "\n", new_gene_b)
        return new_gene_a, new_gene_b

    def evaluate(self):
        pass

    def __repr__(self):
        return "{}".format(self.genome)

class Population:
    def __init__(self):
        self.pop_size = 25
        self.selection_ratio = 0.5
        self.mutation_ratio = 0.05
        self.crossover_ratio = 0.2
        self.population = []

    def regenerate(self):
        self.population = []
        for _ in range(self.pop_size):
            self.population.append(Gene())
        #print(self.population)

    def evaluate(self):
        for each in self.population:
            each.evaluate()

    def selection(self):
        self.population.sort(key = lambda x:x.score, reverse = True)
        self.population = self.population[:self.pop_size//2]

    def crossover(self):
        temp = []
        for i in range(self.pop_size//4):
            a, b = random.sample(self.population, 2)
            print(a, b)
            pos = random.randint(1, d - 2)
            new_a, new_b = a.cross(b, position = pos)
            temp.extend([new_a, new_b])
        self.population.extend([temp])

    def mutate(self):
        temp = []
        for each in self.population:
            if random.random < self.mutation_ratio:
                new_c = each.mutate()
                temp.extend([new_c])
        self.population.extend([temp])

class Zone:
    instances = []

    def __init__(self, I, X, Y):
        self.zone_id = I
        self.x = X
        self.y = Y
        self.radius = 100
        self.control = -1
        self.instances.append(self)

    def update(self, Z):
        self.control = Z

    def show(self):
        print("Zone %s : (%s, %s) - team : %s" % (self.zone_id, self.x, self.y, self.control), file=sys.stderr)


class Team:
    instances = []

    def __init__(self, I):
        self.team_id = I
        self.crew = []
        self.instances.append(self)

    def add_drone(self):
        self.crew.append(Drone(self.team_id))

    def show(self):
        print("Team : %s - Member : %s" % (self.team_id, [d.drone_id for d in self.crew]), file=sys.stderr)

    def update(self):
        for each in self.crew:
            each.set_distances()


class Drone:
    instances = []
    my_drone = []

    def __init__(self, T):
        self.drone_id = len(self.instances)
        self.team = T
        self.x = 0
        self.y = 0
        self.instances.append(self)
        self.distance = {}
        if self.team == id:
            self.my_drone.append(self)

    def update(self, X, Y):
        self.x = X
        self.y = Y

    def show(self):
        print("Team %s - Drone %s - Position (%s, %s)" % (self.team, self.drone_id, self.x, self.y),
              file=sys.stderr)
        for each in self.distance.keys():
            print("         Base %s -> %s" % (each.zone_id, self.distance[each]), file=sys.stderr)

    def set_distances(self):
        for each_point in Zone.instances:
            d = ((self.x - each_point.x) ** 2 + (self.y - each_point.y) ** 2) ** 0.5
            self.distance[each_point] = d

    def go_to_closest(self):
        mini = 20000
        for key, dist in self.distance.items():
            print(key, dist, file=sys.stderr)
            if dist < mini:
                mini = dist
                target = key
        print(target.x, target.y)


# p: number of players in the game (2 to 4 players)
# id: ID of your player (0, 1, 2, or 3)
# d: number of drones in each team (3 to 11)
# z: number of zones on the map (4 to 8)
p, id, d, z = [int(i) for i in input().split()]
for i in range(z):
    # x: corresponds to the position of the center of a zone. A zone is a circle with a radius of 100 units.
    x, y = [int(j) for j in input().split()]
    Zone(i, x, y)

for i in range(p):
    t = Team(i)
    for j in range(d):
        t.add_drone()

pop = Population()
pop.regenerate()
pop.crossover()


# game loop
while True:
    for i in range(z):
        tid = int(input())  # ID of the team controlling the zone (0, 1, 2, or 3) or -1 if it is not controlled. The zones are given in the same order as in the initialization.
        Zone.instances[i].update(tid)

    for i in range(p):  # For each team
        for j in range(d):   # fro each drone of the team
            # dx: The first D lines contain the coordinates of drones of a player with the ID 0, the following D lines those of the drones of player 1, and thus it continues until the last player.
            dx, dy = [int(k) for k in input().split()]
            Team.instances[i].crew[j].update(dx, dy)

    pop.regenerate()

    for i in range(d):

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        # output a destination point to be reached by one of your drones. The first line corresponds to the first of your drones that you were provided as input, the next to the second, etc.
        print("20 20")
