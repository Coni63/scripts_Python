import sys
import math

class robot:
    loop = {'START_POS': 'DIAGNOSIS', 'DIAGNOSIS':'MOLECULES', 'MOLECULES':'LABORATORY', 'LABORATORY':'DIAGNOSIS'}
    def __init__(self):
        self.current_module = 0
        self.eta = 0
        self.score = 0
        self.expertise = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        self.stock = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        self.switched_module = False
        self.queue = []
        self.sample = None
        
    def first_move(self):
        self.switched_module = True
        #print(self.current_module, file=sys.stderr)
        self.go_to(self.loop[self.current_module])
    
    def next_move(self):
        if self.switched_module: # si on a changé de module
            self.switched_module = False
            #self.go_to(self.loop[self.current_module])
            if self.current_module == 'DIAGNOSIS':
                self.explore_samples()
            elif self.current_module == 'MOLECULES':
                flag = self.pick_elem()
                if not flag: # si on n'a pas pris d'elem
                    self.go_to('LABORATORY')
            elif self.current_module == 'LABORATORY':
                if not self.sample is None:
                    self.drop()
                else:
                    self.go_to('DIAGNOSIS')
        else: 
            if self.current_module == 'DIAGNOSIS': # we need only 1 loop in diag module
                self.go_to('MOLECULES')
            if self.current_module == 'MOLECULES':
                flag = self.pick_elem()
                if not flag: # si on n'a pas pris d'elem
                    self.go_to('LABORATORY')
            elif self.current_module == 'LABORATORY':
                if not self.sample is None:
                    self.drop()
                else:
                    self.go_to('DIAGNOSIS')
    
    def drop(self):
        print("CONNECT {}".format(self.sample.ID))
        self.sample = None    
            
    def pick_elem(self):
        if len(self.queue) > 0:
            elem = self.queue.pop(0)
            print('CONNECT {}'.format(elem))
            return True
        else:
            return False
    
    def explore_samples(self):
        print("exploring samples", file=sys.stderr)
        max_health = 0
        sample_to_do = None
        for key, samples in data.instances.items():
            if samples.carried_by == -1:
                if samples.health > max_health:
                    sample_to_do = samples
                    max_health = samples.health
                    self.sample = sample_to_do
        print("best sample to do is", sample_to_do, file=sys.stderr)
        
        for elem, qty in sample_to_do.recipe.items():
            qty_required_in_queue = max(qty-self.stock[elem], 0)
            if qty_required_in_queue > 0:
                self.queue += [elem] * qty_required_in_queue
                
        print(self.queue, file=sys.stderr)
        print("CONNECT {}".format(sample_to_do.ID)) # pick the sample
                
            
    def connect_to(self, module):
        print("CONNECT {}".format(module))
    
    def go_to(self, module):
        self.switched_module = True
        print("GOTO {}".format(module))
    
class particle:
    liste = {}
    def __init__(self, Name):
        self.name = Name
        self.stock = 999
        self.liste[self.name] = self

class data:
    instances = {}
    def __init__(self, ID, carrier, H):
        self.ID = ID
        self.carried_by = carrier
        self.rank = 0
        self.gain = 0
        self.health = H
        self.recipe = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        self.instances[self.ID] = self

# Bring data on patient samples from the diagnosis machine to the laboratory with enough molecules to produce medicine!

particle('A')
particle('B')
particle('C')
particle('D')
particle('E')

player = [robot(), robot()]
me = player[0]

project_count = int(input())
for i in range(project_count):
    a, b, c, d, e = [int(j) for j in input().split()]

counter = 0
# game loop
while True:
    for i in range(2):
        target, eta, score, storage_a, storage_b, storage_c, storage_d, storage_e, expertise_a, expertise_b, expertise_c, expertise_d, expertise_e = input().split()
        player[i].current_module = target
        player[i].eta = int(eta)
        player[i].score = int(score)
        player[i].stock['A'] = int(storage_a)
        player[i].stock['B'] = int(storage_b)
        player[i].stock['C']  = int(storage_c)
        player[i].stock['D']  = int(storage_d)
        player[i].stock['E']  = int(storage_e)
        player[i].expertise['A']  = int(expertise_a)
        player[i].expertise['B']  = int(expertise_b)
        player[i].expertise['C']  = int(expertise_c)
        player[i].expertise['D']  = int(expertise_d)
        player[i].expertise['E']  = int(expertise_e)
        
    available_a, available_b, available_c, available_d, available_e = [int(i) for i in input().split()]
    particle.liste['A'].stock = available_a
    particle.liste['B'].stock = available_b
    particle.liste['C'].stock = available_c
    particle.liste['D'].stock = available_d
    particle.liste['E'].stock = available_e
    
    data.instances = {}
    sample_count = int(input())
    for i in range(sample_count):
        sample_id, carried_by, rank, expertise_gain, health, cost_a, cost_b, cost_c, cost_d, cost_e = input().split()
        sample_id = int(sample_id)
        carried_by = int(carried_by)
        rank = int(rank)
        health = int(health)
        this = data(sample_id, carried_by, health)
        cost_a = int(cost_a)
        cost_b = int(cost_b)
        cost_c = int(cost_c)
        cost_d = int(cost_d)
        cost_e = int(cost_e)
        this.recipe['A'] = cost_a
        this.recipe['B'] = cost_b
        this.recipe['C'] = cost_c
        this.recipe['D'] = cost_d
        this.recipe['E'] = cost_e
        print(sample_id, carried_by,file=sys.stderr)
        
    if counter == 0:
        me.first_move()
    else:
        me.next_move()
    
    counter += 1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    #print("GOTO DIAGNOSIS")
