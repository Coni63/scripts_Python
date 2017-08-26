import sys
import math


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
        if self.team == team_id:
            self.my_drone.append(self)

    def update(self, X, Y):
        self.x = X
        self.y = Y

    def show(self):
        print("Team %s - Drone %s - Position (%s, %s)" % (self.team, self.drone_id, self.x, self.y), file=sys.stderr)
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
p, team_id, d, z = [int(i) for i in input().split()]
for i in range(z):
    # x: corresponds to the position of the center of a zone. A zone is a circle with a radius of 100 units.
    x, y = [int(j) for j in input().split()]
    Zone(i, x, y)

for each in Zone.instances:
    each.show()
print("", file=sys.stderr)

for i in range(p):
    t = Team(i)
    for j in range(d):
        t.add_drone()

for each in Team.instances:
    each.show()
print("", file=sys.stderr)

# game loop
while True:
    for i in range(z):
        tid = int(
            input())  # ID of the team controlling the zone (0, 1, 2, or 3) or -1 if it is not controlled. The zones are given in the same order as in the initialization.
        Zone.instances[i].update(tid)

    for each in Zone.instances:
        each.show()
    print("", file=sys.stderr)

    for i in range(p):
        for j in range(d):
            # dx: The first D lines contain the coordinates of drones of a player with the ID 0, the following D lines those of the drones of player 1, and thus it continues until the last player.
            dx, dy = [int(k) for k in input().split()]
            Team.instances[i].crew[j].update(dx, dy)

    for each in Drone.instances:
        each.show()

    my_team = Team.instances[team_id]
    # my_team.update()

    for each in Drone.instances:
        each.set_distances()

    for each in my_team.crew:
        each.go_to_closest()
