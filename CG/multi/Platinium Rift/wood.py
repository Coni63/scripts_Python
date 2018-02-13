import sys
import math

class Zone:
    instances = {}
    def __init__(self, ID, platinum):
        self.ID = ID
        self.platinum = platinum
        self.instances[ID] = self
        self.link = []
        self.owner = None
        self.pods = []  # pods per team
        
    def add_link(self, other_area):
        self.link.append(other_area)
        
    def __repr__(self):
        return "Zone {} - Platinum: {}".format(self.ID, self.platinum)


class Player:
    def __init__(self):
        self.pods = {}
        self.zones = []
        self.platinum = 200
    
    @property
    def score(self):
        return len(self.zones)
        
    def show(self):
        print("PODS", file=sys.stderr)
        for key, value in self.pods.items():
            print(key, value, file=sys.stderr)
    
    def move(self):
        move_list = []
        for zone, nb_pods in self.pods.items():
            free_area = []
            for neighbor in zone.link:
                if neighbor.owner == -1:
                    free_area.append(neighbor)
            valid_move = min(nb_pods, len(free_area))
            for i in range(valid_move):
                dest = free_area.pop(0)
                move_list += [1, zone.ID, dest.ID]  # pods, origin, dest
        
        if len(move_list) > 0:
            move_list = map(str, move_list)
            print(" ".join(move_list))
        else:
            print("WAIT")
    
    def conquer(self):
        result = []
        possible_spawn = filter(lambda x: x.owner == -1, Zone.instances.values())
        best_areas = sorted(possible_spawn, key = lambda x : x.platinum, reverse = True)
        possible_pods = me.platinum//20
        nb_valid = min(possible_pods, len(best_areas))
        for i in range(nb_valid):
            area = best_areas.pop(0)
            result += [1, area.ID]
        if len(result) > 0:
            result = map(str, result)
            print(" ".join(result))
        else:
            print("WAIT")
            
    
    def first_turn(self):
        result = []
        best_areas = sorted(Zone.instances.values(), key = lambda x : x.platinum, reverse = True)
        for i in range(5):
            area = best_areas.pop(0)
            result += [2, area.ID]
        result = map(str, result)
        print("WAIT")
        print(" ".join(result))
    
    def play(self):
        self.move()
        self.conquer()
            
        

# player_count: the amount of players (2 to 4)
# my_id: my player ID (0, 1, 2 or 3)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: the amount of Platinum this zone can provide per game turn
    zone_id, platinum_source = [int(j) for j in input().split()]
    Zone(zone_id, platinum_source)
    

for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    z1 = Zone.instances[zone_1]
    z2 = Zone.instances[zone_2]
    z1.add_link(z2)
    z2.add_link(z1)

me = Player()
turn = 0
while True:
    platinum = int(input())  # my available Platinum
    me.platinum = platinum
    me.zones = []
    me.pods = {}
    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # pods_p2: player 2's PODs on this zone (always 0 for a two player game)
        # pods_p3: player 3's PODs on this zone (always 0 for a two or three player game)
        z_id, owner_id, *pods = [int(j) for j in input().split()]
        zone = Zone.instances[z_id]
        zone.owner = owner_id
        zone.pods = pods
        if owner_id == my_id:
            me.zones.append(zone)
        if pods[my_id] > 0:
            me.pods[zone] = pods[my_id]

    # print(me.show(), file=sys.stderr)
    
    if turn == 0:
        me.first_turn()
    else:
        me.play()
        
    turn += 1