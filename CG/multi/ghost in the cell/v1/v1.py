import sys
import math
from collections import defaultdict, deque
from time import time



def clear_risk_of_impact():
    for i in range(len(Bomb.enemy_bomb)):
        if not Bomb.enemy_bomb[i] in Bomb.enemy_ongoing_bomb: #si la bombe a impacté
             for each_bases in Factory.my_bases.values():
                each_bases.risk[i] = 0

def defend_my_bases():
    ordered_bases = sorted(Factory.my_bases.values(), key=lambda obj:obj.defense, reverse=True)
    #print([a.ID for a in ordered_bases], file=sys.stderr)
    support_queue = []
    for each_bases in ordered_bases:
        potential = each_bases.defense - each_bases.required_def
        if potential > 1:
            for each_other_bases in ordered_bases:
                if each_other_bases != each_bases: 
                    remaining_army = each_other_bases.defense + each_other_bases.ongoing_support - each_other_bases.required_def
                    if remaining_army <= 2:
                        support = min(potential, 2-remaining_army)
                        potential -= support
                        support_queue.append((each_bases.ID, each_other_bases.ID, support))
    return support_queue

def set_list_of_targets():
    main_queue = []
    for key, factory in Factory.my_bases.items():
        a = []
        safety = 1
        number_of_robot = factory.defense
        queue = []
        
        for each_voisin in G.edges[key]:
            a.append((each_voisin, G.distances[(key, each_voisin)]))
        a.sort(key=lambda a:a[1]) #tri par distances des noeuds voisins
        
        for each_node in a:
            node_id = each_node[0]
            if Factory.instances[node_id].prod > 0:
                if Factory.instances[node_id].team == 0:
                    qte = Factory.instances[node_id].defense
                    if number_of_robot >= qte + safety:
                        queue.append((key, node_id, qte + safety))
                        number_of_robot -= qte + safety
                elif Factory.instances[node_id].team == 1:
                    pass
                else:
                    qte = Factory.instances[node_id].defense
                    additionnal = G.distances[(key, node_id)] * Factory.instances[node_id].prod
                    if qte + additionnal + safety <= number_of_robot:
                        queue.append((key, node_id, qte + additionnal + safety))
                        number_of_robot -= qte + additionnal + safety
        main_queue += queue
    return main_queue

def check_best_target():
    maxi = 11 #ne pas envoyer avant 11 each.defense > maxi and
    target = None
    base = None
    for each in Factory.opponents_bases.values():
        if each.prod >= 2 and each.ID not in Bomb.my_bomb:
            target = each.ID
    
    if not target is None:
        mini = 21
        for each in Factory.my_bases.values():
            if G.distances[(each.ID, target)] < mini:
                base = each.ID
    
    return target, base
            
def set_states():
    for each in Factory.my_bases.values():
        productivity[0] += each.prod
        scores[0] += each.defense
    for each in Factory.opponents_bases.values():
        productivity[1] += each.prod
        scores[1] += each.defense
    for each in Cyborg.my_robots.values():
        scores[0] += each.troop_size
    for each in Cyborg.ennemies.values():
        scores[1] += each.troop_size
    base_controlled = [len(Factory.my_bases), len(Factory.opponents_bases), len(Factory.free_bases)]
    
def check_for_base_update(current_loop):
    update_list = []
    for each in Factory.my_bases.values():
        if each.prod < 3 and each.defense > 30 and current_loop < 300:
            update_list.append(each.ID)
    return update_list

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.links = 0

    def ajouteSommet(self, sommet):
        if sommet not in self.nodes:
            self.nodes.add(sommet)

    def ajouteArrete(self, sommet, sommetVoisin, dist=1):
        if sommet != sommetVoisin:
            self.edges[sommetVoisin].append(sommet) 
            self.edges[sommet].append(sommetVoisin)
            self.distances[(sommet, sommetVoisin)] = dist
            self.distances[(sommetVoisin, sommet)] = dist
            self.links += 1
    
    def show(self):
        for key, value in self.distances.items():
            print("%s -> %s : %s tour" % (key[0], key[1], value) ,file=sys.stderr)
       
class Factory:
    instances = {}
    my_bases = {}
    opponents_bases = {}
    free_bases = {}
    def __init__(self, ID, team, defense, prod):
        if team == 1 :
            self.my_bases[ID] = self
        elif team == -1:
            self.opponents_bases[ID] = self
        else:
            self.free_bases[ID] = self
        self.ID = ID
        self.team = team
        self.defense = defense
        self.prod = prod
        self.instances[ID]=self
        self.required_def = 0
        self.ongoing_support = 0
        self.risk = [0, 0]
    
    def update(self, team, defense, prod):
        if team == 1 :
            self.my_bases[self.ID] = self
        elif team == -1:
            self.opponents_bases[self.ID] = self
        else:
            self.free_bases[self.ID] =self
        self.team = team
        self.defense = defense
        self.prod = prod
        self.required_def = 0
        self.ongoing_support = 0
        self.risk[0] = max(0, self.risk[0]-1)
        self.risk[1] = max(0, self.risk[1]-1)
        
    def show(self):
        print(self.__dict__, file=sys.stderr)
                  
class Cyborg:
    instances = {}
    my_robots = {}
    ennemies = {}
    def __init__(self, ID, team, s, e, num, t):
        if team == 1 :
            self.my_robots[ID] = self
            self.team = "me"
            if e in Factory.my_bases.keys():
                Factory.my_bases[e].ongoing_support += num
        else:
            self.ennemies[ID] = self
            self.team = "opponent"
            if e in Factory.my_bases.keys():
                Factory.my_bases[e].required_def += num
        self.ID = ID
        self.s_factory = s
        self.e_factory = e
        self.troop_size = num
        self.remaining_turn = t
        self.instances[ID] = self
    
    def show(self):
        print(self.__dict__, file=sys.stderr)

class Bomb:
    instances = {}
    my_bomb = []
    enemy_bomb = [] #ID des bombes ennemies pour savoir si c'est une nouvelle bombe
    enemy_ongoing_bomb = []
    def __init__(self, ID, t, s, e):
        self.ID = ID
        self.team = t
        self.start = s
        self.end = e
        self.instances[ID] = self
        if t == 1:
            self.my_bomb.append(e)
        if t == -1:
            self.enemy_ongoing_bomb.append(ID)
            if not ID in self.enemy_bomb:
                self.enemy_bomb.append(ID)
                bomb_number = len(self.enemy_bomb)-1
                for each_bases in Factory.my_bases.values():
                    d = G.distances[(s, each_bases.ID)]
                    each_bases.risk[bomb_number] = d
    
    def show(self):
        print(self.__dict__, file=sys.stderr)


start_init_time = time()
G = Graph()

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    G.ajouteSommet(factory_1)
    G.ajouteSommet(factory_2)
    G.ajouteArrete(factory_1, factory_2, distance)

#G.show()
#print(G.links, link_count, file=sys.stderr)

first_loop = True
loop = 0
bomb = 2
while True:
    start_time = time()
    Factory.my_bases = {}
    Factory.opponents_bases = {}
    Factory.free_bases = {}
    Cyborg.instances = {}
    Cyborg.my_robots = {}
    Cyborg.ennemies = {}
    Bomb.my_bomb = []
    Bomb.enemy_ongoing_bomb = []
    scores = [0, 0] #moi et ennemie
    productivity = [0, 0]#moi et ennemie
    base_controlled = [0, 0, 0]
    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    for i in range(entity_count):
        entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = input().split()
        entity_id = int(entity_id)
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)
        arg_5 = int(arg_5)
        if entity_type == "FACTORY":
            if not entity_id in Factory.instances.keys():
                Factory(entity_id, arg_1, arg_2, arg_3)
            else :
                Factory.instances[entity_id].update(arg_1, arg_2, arg_3)
        elif entity_type == "TROOP":
            #print(entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5, file=sys.stderr)
            Cyborg(entity_id, arg_1, arg_2, arg_3, arg_4, arg_5)
        elif entity_type == "BOMB":
            Bomb(entity_id, arg_1, arg_2, arg_3)
    
    set_states()
    print(scores, productivity ,file=sys.stderr)  
    
    clear_risk_of_impact()    
    #print("",file=sys.stderr)
    #for each in Cyborg.my_robots.values():
    #    each.show()
    #print("",file=sys.stderr)
    #for each in Cyborg.ennemies.values():
    #    each.show()
    #print("",file=sys.stderr)
    for each in Factory.my_bases.values():
        each.show()
    #print("",file=sys.stderr)
    #for each in Factory.instances.values():
    #    each.show()
    #print("",file=sys.stderr)
    #for each in Bomb.instances.values():
    #    each.show()
            
    if (base_controlled[0] > base_controlled[1]) or (base_controlled[0] == base_controlled[1] and productivity[0] > productivity[1]) or (base_controlled[0] == base_controlled[1] and productivity[0] == productivity[1] and scores[0] > scores[1]):
        main_queue = defend_my_bases()
    else:
        main_queue = set_list_of_targets()
    #print(main_queue ,file=sys.stderr)  
    
    if main_queue == []:
        command = "WAIT"
    else:
        command = ";".join(["MOVE %s %s %s"% (each[0], each[1], each[2]) for each in main_queue])
    
    if bomb > 0: # and loop > 30:
        target, base = check_best_target()
        if not target is None:
            command += ";BOMB %s %s"%(base, target)
            bomb -= 1
    
    if scores[0] > scores[1] + 20:
            base_to_update = check_for_base_update(loop)
            if base_to_update != []:
                for each in base_to_update:
                    command += ";INC %s" %(each)
    
    for each_base in Factory.my_bases.values():
        if each_base.risk[0] == 1 or each_base.risk[1] == 1:
            closest = 21
            target = None
            for each_other_base in Factory.my_bases.values():
                if each_base != each_other_base:
                    d = G.distances[(each_base.ID, each_other_base.ID)]
                    qte = each_base.defense
                    if d < closest:
                        closest = d
                        target = each_other_base.ID
            if target is None:
                smallest = 10000
                qte = each_base.defense
                for other_base in Factory.opponents_bases.values():
                    if other_base.defense < smallest:
                        smallest = other_base.defense
                        target = other_base.ID
            command += ";MOVE %s %s %s" %(each_base.ID, target, qte)
    
    command += ";MSG tour: %s - time: %.4s ms" %(loop, (time()-start_time)*1000)
    print(command)
    loop += 2 
    
    if first_loop:
        print(time()-start_init_time, file=sys.stderr)
        first_loop = False
    else:
        print(time()-start_time, file=sys.stderr)
    
    
    
    
    
   
