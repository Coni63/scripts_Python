import sys
import math
import random

class Zone:
    instances = {}
    def __init__(self, ID, platinum):
        self.ID = ID
        self.platinum = platinum
        self.instances[ID] = self
        self.link = []
        self.owner = None
        self.pods = []  # pods per team

    @property
    def is_bottleneck(self):
        return len(self.link) <= 2

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

    def evaluate_moves(self, zone, nb_pods=1):
        score = {}
        for neighbor in zone.link:
            if neighbor.owner == -1:
                score[neighbor] = 1
            elif neighbor.owner not in [-1, my_id]:
                other_pods = neighbor.pods
                if sum(other_pods) == 0:
                    score[neighbor] = 2
                if nb_pods > max(other_pods):
                    score[neighbor] = 5
            else:
                score[neighbor] = 0
        return score

    def pick_move(self, moves):
        if len(moves) == 0: # si on est bloqué dans un coin avec un pion a coté
            dest = -1
        elif sum(moves.values()) == 0: # on a que des moves dans la zone a nous
            dest = random.choice(list(moves.keys()))
        else:
            dest = max(moves.items(), key = lambda x: x[1])[0]
        return dest


    def expand(self):
        move_list = []
        for zone, nb_pods in self.pods.items():
            moves = self.evaluate_moves(zone, nb_pods)
            dest = self.pick_move(moves)
            if dest != -1:
                move_list += [nb_pods, zone.ID, dest.ID]

        if len(move_list) > 0:
            move_list = map(str, move_list)
            print(" ".join(move_list))
        else:
            print("WAIT")


    def get_number_of_pods_craftable(self):
        return me.platinum//20

    def check_best_positions(self):
        possible_spawn = filter(lambda x: x.owner == -1, Zone.instances.values())
        best_areas = sorted(possible_spawn, key=lambda x: x.platinum, reverse=True)
        return best_areas

    def check_my_areas_close_to_enemies(self):
        my_areas = filter(lambda x: x.owner == my_id, Zone.instances.values())
        best_spawn = 0
        best_score = 0
        for each_area in my_areas:
            moves = self.evaluate_moves(each_area)
            score = sum(moves.values())
            if score > best_score:
                score = best_score
                best_spawn = each_area
        return best_spawn

    def spawn(self):
        nb_pods = self.get_number_of_pods_craftable()
        result = []
        if nb_pods > 0:
            best_areas = self.check_best_positions()
            if len(best_areas) > 0:
                if len(best_areas) >= nb_pods:
                    for i in range(nb_pods):
                        area = best_areas.pop(0)
                        result += [1, area.ID]
                elif len(best_areas) < nb_pods:
                    qte_list = share(nb_pods, len(best_areas))
                    for i in range(len(best_areas)):
                        area = best_areas.pop(0)
                        qte = qte_list.pop(0)
                        result += [qte, area.ID]
            else:
                spawn = self.check_my_areas_close_to_enemies()
                result += [nb_pods, spawn.ID]

        if len(result) > 0:
            result = map(str, result)
            print(" ".join(result))
        else:
            print("WAIT")
            
    
    # def first_turn(self):
    #     self.first_turn2()
    #     result = []
    #     best_areas = sorted(Zone.instances.values(), key = lambda x : x.platinum, reverse = True)
    #     for i in range(10):
    #         area = best_areas.pop(0)
    #         result += [1, area.ID]
    #     result = map(str, result)
    #     print("WAIT")
    #     print(" ".join(result))


    def first_turn(self):
        best_areas = []
        result = []
        for z in Zone.instances.values():
            if z.is_bottleneck:
                best_areas.append(z)
        best_areas.sort(key = lambda x : x.platinum, reverse = True)
        for i in range(10):
            area = best_areas.pop(0)
            result += [1, area.ID]
        result = map(str, result)
        print("WAIT")
        print(" ".join(result))


    def play(self):
        self.expand()
        self.spawn()

def share(n_elem, size):
    shared = [0] * size
    for i in range(size):
        qte = n_elem // (size-i)
        shared[i] = qte
        n_elem -= qte
    return shared


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
        
    turn += 7
