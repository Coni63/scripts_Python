import sys
import math

class robot:
    loop = {'START_POS': 'SAMPLES', 'SAMPLES': 'DIAGNOSIS', 'DIAGNOSIS':'MOLECULES', 'MOLECULES':'LABORATORY', 'LABORATORY':'DIAGNOSIS'}
    wait_turn = {
        'START_POS' : {'START_POS': 2 , 'SAMPLES': 2 , 'DIAGNOSIS': 2 ,  'MOLECULES': 2 , 'LABORATORY': 2},
        'SAMPLES' :  {'START_POS': 0 , 'SAMPLES': 0 , 'DIAGNOSIS': 3 ,  'MOLECULES': 3 , 'LABORATORY': 3},
        'DIAGNOSIS' :  {'START_POS': 0 , 'SAMPLES': 3 , 'DIAGNOSIS': 0 ,  'MOLECULES': 3 , 'LABORATORY': 4},
        'MOLECULES' :  {'START_POS': 0 , 'SAMPLES': 3 , 'DIAGNOSIS': 3 ,  'MOLECULES': 0 , 'LABORATORY': 3},
        'LABORATORY' :  {'START_POS': 0 , 'SAMPLES': 3 , 'DIAGNOSIS': 4 ,  'MOLECULES': 3 , 'LABORATORY': 0},
    }
    def __init__(self):
        self.current_module = 0
        self.eta = 0
        self.score = 0
        self.expertise = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        self.stock = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        self.queue = []
        self.sample_list = []
        self.has_dropped = False
        self.analysed = []
        self.wait = 0

    def next_move(self):
        if self.wait == 0:
            if self.current_module == 'SAMPLES':
                self.check_qty_of_samples()
                if len(self.sample_list) < 3:
                    self.explore_samples()
                else:
                    self.go_to('DIAGNOSIS')
            elif self.current_module == 'DIAGNOSIS':
                finished = True
                for elem in self.sample_list:
                    if elem.status == 'undiagnosed' and not elem in self.analysed:
                        self.analyse(elem)
                        finished = False
                        break
                if finished:
                    self.go_to('MOLECULES')
            elif self.current_module == 'MOLECULES':
                self.set_queue()
                current_qty = sum(list(self.stock.values()))
                if len(self.queue[0]) > 0:
                    self.pick_elem()
                else:
                    self.go_to('LABORATORY')
            elif self.current_module == 'LABORATORY':
                if len(self.sample_list) > 0:
                    if not self.has_dropped:
                        self.has_dropped = True
                        self.drop()
                    else:
                        self.has_dropped = False
                        self.go_to('MOLECULES')
                else:
                    self.go_to('SAMPLES')
        else:
            self.wait = max(self.wait-1, 0)
            print("WAIT")

    def analyse(self, sample):
        #sample.status = 'diagnosed'
        self.analysed.append(sample)
        print("CONNECT {}".format(sample.ID))

    def drop(self):
        elem = self.sample_list.pop(0)
        elem.released = True
        print("CONNECT {}".format(elem.ID))
            
    def pick_elem(self):
        loop = 0
        picked = False
        while loop < 10 and picked == False:
            elem = self.queue[0].pop(0)
            if particle.liste[elem].stock > 0:
                print('CONNECT {}'.format(elem))
                picked = True
            else:
                self.queue[0].append(elem)
                loop += 1
        if not picked:
            #print('CONNECT {}'.format(self.queue[0][0]))
            print("WAIT")


    def check_qty_of_samples(self):
        self.sample_list = []
        for key, item in data.instances.items():
            if item.carried_by == 0 and not item.released:
                self.sample_list.append(item)

    def set_queue(self):
        #print( self.sample_list, file=sys.stderr)
        self.queue = []
        for sample in self.sample_list:
            queue_sample = []
            for elem, qty in sample.recipe.items():
                #print(elem, qty, file=sys.stderr)
                qty_required_in_queue = max(qty - self.stock[elem] - self.expertise[elem], 0)
                if qty_required_in_queue > 0:
                    queue_sample += [elem] * qty_required_in_queue
            self.queue.append(queue_sample)
        print(self.queue, file=sys.stderr)

    def explore_samples(self):
        print("CONNECT {}".format(2))  # pick the sample

    def connect_to(self, module):
        print("CONNECT {}".format(module))
    
    def go_to(self, target_module):
        self.wait = self.wait_turn[self.current_module][target_module]-1
        print("GOTO {}".format(target_module))
    
class particle:
    liste = {}
    def __init__(self, Name):
        self.name = Name
        self.stock = 999
        self.liste[self.name] = self

class data:
    instances = {}
    def __init__(self, ID):
        self.ID = ID
        self.carried_by = -1
        self.rank = 0
        self.gain = 0
        self.health = 0
        self.recipe = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        self.instances[self.ID] = self
        self.released = False

    def set_status(self):
        if sum(self.recipe.values()) > 0:
            self.status = 'diagnosed'
        else:
            self.status = 'undiagnosed'

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
    print(a, b, c, d, e, file=sys.stderr)

first_loop = True
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

    #print(me.stock, me.expertise, file=sys.stderr)
        
    available_a, available_b, available_c, available_d, available_e = [int(i) for i in input().split()]
    particle.liste['A'].stock = available_a
    particle.liste['B'].stock = available_b
    particle.liste['C'].stock = available_c
    particle.liste['D'].stock = available_d
    particle.liste['E'].stock = available_e
    #print(available_a, available_b, available_c, available_d, available_e , file=sys.stderr)

    sample_count = int(input())
    for i in range(sample_count):
        sample_id, carried_by, rank, expertise_gain, health, cost_a, cost_b, cost_c, cost_d, cost_e = input().split()
        sample_id = int(sample_id)
        if sample_id in data.instances.keys():
            this = data.instances[sample_id]
        else:
            this = data(sample_id)
        carried_by = int(carried_by)
        rank = int(rank)
        health = int(health)
        cost_a = int(cost_a)
        cost_b = int(cost_b)
        cost_c = int(cost_c)
        cost_d = int(cost_d)
        cost_e = int(cost_e)

        this.set_status()

        this.carried_by = carried_by
        this.rank = rank
        this.health = health
        this.gain = expertise_gain
        this.recipe['A'] = cost_a
        this.recipe['B'] = cost_b
        this.recipe['C'] = cost_c
        this.recipe['D'] = cost_d
        this.recipe['E'] = cost_e
        #print(sample_id, carried_by, this.recipe, this.status, this.released, file=sys.stderr)
        
    if first_loop:
        me.go_to('SAMPLES')
        first_loop = False
    else:
        me.next_move()
