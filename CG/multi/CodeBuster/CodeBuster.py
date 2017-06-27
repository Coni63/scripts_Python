import sys
import math
from time import time
import random

class Entity:
    def __init__(self, _position, _ID, _team, _state, _value):
        self.position = _position
        self.ID = _ID
        self.team = _team
        self.state = _state
        self.value = _value
        
    def update(self, _position, _state, _value):
        self.position = _position
        self.state = _state
        self.value = _value
    
        
class Ghost(Entity):
    ghost_list = {}
    def __init__(self, _position, _ID, _team, _state, _value):
        super().__init__(_position, _ID, _team, _state, _value)
        self.ghost_list[_ID] = self
        
    def show(self):
        print(self.__dict__, file=sys.stderr)
        
        
class Buster(Entity):
    enemy_busters = {}
    my_busters = {}
    def __init__(self, _position, _ID, _team, _state, _value, _h):
        super().__init__(_position, _ID, _team, _state, _value)
        self.reloading = 0
        self.height = int(_h)
        self.explored_all = False
        self.next_position = None
        self.need_help = 0
        self.target = None
        self.role = None
        self.take_ghost = False
        self.cover_pos = (0,0)
        if _team == my_team_id:
            self.my_busters[_ID] = self
        else :
            self.enemy_busters[_ID] = self
    
    def update(self, _position, _state, _value):
        super().update(_position, _state, _value)
        self.reloading = max(self.reloading-1, 0)
        
    def display(self):
        attrs = vars(self)
        print( ', '.join("%s: %s" % item for item in attrs.items()), file = sys.stderr)
    
    def distance_to(self, item):
        X2 = (self.position[0] - item[0])**2
        Y2 = (self.position[1] - item[1])**2
        return math.sqrt(X2+Y2)
    
    def go_to(self, target, text=""):
        print("MOVE %s %s %s"%(target[0], target[1], text))
        
    def explore(self):
        if not self.explored_all:
            dy = self.position[1]-self.height
            if my_team_id == 0:
                if abs(dy) >= 800:
                    self.go_to((1760, self.height))
                else:
                    dx = int(math.sqrt(800**2-dy**2))
                    self.go_to((self.position[0]+dx, self.height))
                    if self.position[0]+dx >= parcours:
                        self.explored_all = True
            else :
                if abs(dy) >= 800:
                    self.go_to((16000-1760, self.height))
                else:
                    dx = int(math.sqrt(800**2-dy**2))
                    self.go_to((self.position[0]-dx, self.height))
                    if self.position[0]+dx <= 16000-parcours:
                        self.explored_all = True
        else:
            """
            self.role = "basecamp"            
            self.go_to(camp_pos[my_team_id])
            self.next_position = camp_pos[my_team_id]
            """
            if self.next_position is None:
                self.next_position = (1000*random.randint(1,15), 1000*random.randint(1,8))
                self.go_to(self.next_position)
            else:
                if self.distance_to(self.next_position) < 800:
                    self.next_position = (1000*random.randint(1,15), 1000*random.randint(1,8))
                    self.go_to(self.next_position)
                else:
                    self.go_to(self.next_position)
            
                           
    def check_for_support(self):
        if self.target!=None:
            if 900 < self.distance_to(self.target[1]) < 1760:
                print("BUST %s" % self.target[0])
                return True
            elif self.distance_to(self.target[1]) < (1500+5*800):
                self.go_to(self.target[1], "I'm coming")
                return True
        else:    
            for ID_b, buster in Buster.my_busters.items():
                if buster != self and buster.need_help > 0:
                    buster.need_help -= 1
                    self.target = buster.target
                    if 900 < self.distance_to(self.target[1]) < 1760:
                        print("BUST %s" % self.target[0])
                    else:
                        self.go_to(self.target[1], "I'm coming")
                    return True
        return False
        
    def is_busting(self):
        if self.state == 3:
            if self.target !=None:
                dist = self.distance_to(self.target[1])
                if 900 < dist < 1760:
                    print("BUST %s eat that :)" % self.target[0])
                elif dist >= 1760:
                    self.go_to(self.target[1])
                else:
                    new_x = (1200/dist)*(self.position[0]-self.target[1][0])+self.target[1][0]
                    new_y = (1200/dist)*(self.position[1]-self.target[1][1])+self.target[1][1]
                    self.go_to((new_x, new_y))
                    
                if Ghost.ghost_list[self.target[0]].state == 0:
                    self.need_help += 1
                return True
        return False
        
    def is_stunned(self):
        if self.state == 2:
            print("MOVE 0 0 I'm drunk !")
            return True
        return False
        
    def carry_ghost(self):
        if self.state == 1: 
            if self.distance_to(BP) > 1600:
                self.go_to(BP)
            else:
                print("RELEASE You stay here !")
            return True
        return False

    def stun(self, with_ghost=False):
        if self.state == 0 and self.reloading == 0:
            for ID, buster in Buster.enemy_busters.items():
                if self.distance_to(buster.position) < 1760 and buster.state != 2:
                    if (with_ghost == True and buster.state == 1) or (with_ghost == False):
                        print("STUN %s" % buster.ID)
                        self.reloading = 20
                        #if self.role == "basecamp":
                        #    self.stunned_ID = buster.value
                        return True
        return False
                
    def check_for_ghost(self):
        possible_ghost = []
        visible_ghost = []
        for ID_g, ghost in Ghost.ghost_list.items():
            d_ghost = self.distance_to(ghost.position)
            if d_ghost <= 2200:  #si c'est moi qui voit le ghost
                if 900 < d_ghost < 1760: #je verifie que je suis à portée, sinon je le stocke juste dans visible
                    possible_ghost.append(ghost)
                else:
                    visible_ghost.append(ghost)
        if len(possible_ghost) > 0: #si j'ai des ghosts a portée
            ghost_selected = min(possible_ghost, key=lambda x: x.state)
            self.target = (ghost_selected.ID, ghost_selected.position)
            if ghost_selected.state >= 10:
                if ghost_selected.state >= 30:
                    self.need_help = min(2, busters_per_player-1)
                else:
                    self.need_help = 1
                print("BUST %s I'll need help" % ghost_selected.ID)
            else:
                print("BUST %s found %s" % (ghost_selected.ID, ghost_selected.ID))
            return True
        elif len(possible_ghost) == 0 and len(visible_ghost) > 0:
            ghost_selected = min(visible_ghost, key=lambda x: x.state)
            self.go_to(ghost_selected.position)
            return True
        else:
            return False
    
    def basecamp(self):
        if self.state == 1:
            self.go_to(BP)
            #self.take_ghost = False
        else:
            if self.stun(with_ghost = True) == False:
                if self.check_for_ghost() == False:
                    self.cover()
        """
        elif self.take_ghost:
            if self.stunned_ID != -1:
                print("BUST %s you are mine" % self.stunned_ID)
            else:
                self.cover()
                #self.go_to(camp_pos[my_team_id])
        else:
            #if self.distance_to(camp_pos[my_team_id]) < 800:        
                if self.stun(with_ghost = True) == False:
                    self.cover()
                else:
                    if self.state != 2: self.take_ghost = True
            else:
                self.go_to(camp_pos[my_team_id])
        """

    def cover(self):
        if my_team_id == 0:
            if self.distance_to((13000,8000)) < 400:
                self.go_to((15000, 6000))
                self.next_position = (15000, 6000)
            elif self.distance_to((15000, 6000)) < 400:
                self.go_to((13000,8000))
                self.next_position = (13000,8000)
            else:
                self.go_to(self.next_position)
        else:
            if self.distance_to((3000,1000)) < 400:
                self.go_to((1000, 3000))
                self.next_position = (1000, 3000)
            elif self.distance_to((1000, 3000)) < 400:
                self.go_to((3000,1000))
                self.next_position = (3000,1000)
            else:
                self.go_to(self.next_position)
                
    def show(self):
        print(self.__dict__, file=sys.stderr)

def review_targets():
    for ID_b, buster in Buster.my_busters.items():
        if buster.target != None:
            g_list = Ghost.ghost_list.keys() 
            if not buster.target[0] in g_list:
                buster.need_help = 0                
                buster.target = None

def review_help():
    for ID_b, buster in Buster.my_busters.items(): 
        if buster.state == 1:                       #si mon buster carry un ghost
            buster.need_help = 0                    #alors il n'a plus besoin d'aide
            buster.target = None
            for id_b, b in Buster.my_busters.items():      #on verifie alors pour tous mes busters
                if b.target != None: 
                    if b.target[0] == buster.value:      #si leur target est le ghost que l'on transporte
                        b.target = None            #alors on retire la target
                        b.need_help = 0        #et il n'a plus beoisn d'aide
            
busters_per_player = int(input())  # the amount of busters you control
ghost_count = int(input())  # the amount of ghosts on the map
my_team_id = int(input())  # if this is 0, your base is on the top left of the map, if it is one, on the bottom right

BP = (my_team_id*16000, my_team_id*9000)

if busters_per_player == 2:
    gen_y = [3500, 5500]#[2200, 6800]
elif busters_per_player == 3:
    gen_y = [3500, 4500, 5500] #[1500, 4500 ,7500]
elif busters_per_player == 4:
    gen_y = [3500, 4500, 4500, 5500] #[1500, 3000, 4500, 7500]
else:
    gen_y = [3500, 4500, 4500, 4500 ,5500] #[1000, 2500, 4000, 6500, 8000]
    
shift = 1500
camp_pos= [(13000, 8000), (3000, 1000)] #[(16000-shift, 9000-shift), (shift, shift)]
parcours = 8000

time_history = []
turn = 0

while True:
    start = time()
    
    entities = int(input())  # the number of busters and ghosts visible to you
    for i in range(entities):
        # entity_id: buster id or ghost id
        # y: position of this buster / ghost
        # entity_type: the team id if it is a buster, -1 if it is a ghost.
        # state: For busters: 0=idle, 1=carrying a ghost.
        # value: For busters: Ghost id being carried. For ghosts: number of busters attempting to trap this ghost.
        entity_id, x, y, entity_type, state, value = [int(j) for j in input().split()]

        if entity_type == -1:
            if entity_id in Ghost.ghost_list.keys():
                Ghost.ghost_list[entity_id].update((x, y), state, value)
            else:
                Ghost((x, y), entity_id, entity_type, state, value)
        elif entity_type == my_team_id:
            if entity_id in Buster.my_busters.keys():
                Buster.my_busters[entity_id].update((x, y), state, value)
            else:    
                Buster((x, y), entity_id, entity_type, state, value, gen_y.pop(0))
        else:
            if entity_id in Buster.enemy_busters.keys():
                Buster.enemy_busters[entity_id].update((x, y), state, value)
            else:
                Buster((x, y), entity_id, entity_type, state, value)
    
    #if busters_per_player > 2 and turn > 100:
    #    index = list(Buster.my_busters.keys())[-1]
    #    Buster.my_busters[index].role = "basecamp"
    
    #for each in Ghost.ghost_list.values():
    #    each.show()
    
    Ghost.ghost_list = {}
    
    review_help()
    review_targets()
    for ID_b, buster in Buster.my_busters.items():
        buster.show()
        if buster.role is None:
            if buster.is_stunned() == False:
                if buster.carry_ghost() == False:
                    if buster.stun() == False:
                        if buster.is_busting() == False:
                            if buster.check_for_support() == False:
                                if buster.check_for_ghost() == False:
                                    buster.explore()
        else:
            buster.basecamp()
                                                
    duration = (time()-start)*1000
    if turn > 0:
        time_history.append(duration)
        print("time {:06.2f} ms (min {:06.2f}ms - max {:06.2f}ms - avg {:06.2f}ms)".format(duration, min(time_history), max(time_history), sum(time_history)/len(time_history) ), file=sys.stderr)
    turn +=1