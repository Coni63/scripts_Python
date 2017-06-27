import sys
import math

class robot:
    loop = {'START_POS': 'SAMPLES', 'SAMPLES': 'DIAGNOSIS', 'DIAGNOSIS':'MOLECULES', 'MOLECULES':'LABORATORY', 'LABORATORY':'DIAGNOSIS'}
    def __init__(self):
        self.current_module = 0
        self.eta = 0
        self.score = 0
        self.expertise = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        self.stock = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        self.queue = []
        self.sample_list = []
        self.has_dropped = False

    def first_move(self):
        self.go_to(self.loop[self.current_module])
    
    def next_move(self):
        if self.current_module == 'SAMPLES':
            self.check_qty_of_samples()
            if len(self.sample_list) < 3:
                self.explore_samples()
                #self.go_to('DIAGNOSIS')
            else:
                self.go_to('DIAGNOSIS')
        elif self.current_module == 'DIAGNOSIS':
            finished = True
            for elem in self.sample_list:
                if elem.status == 'undiagnosed':
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

    def analyse(self, sample):
        sample.status = 'diagnosed'
        print("CONNECT {}".format(sample.ID))

    def drop(self):
        elem = self.sample_list.pop(0)
        elem.status = 'researched'
        print("CONNECT {}".format(elem.ID))
            
    def pick_elem(self):
        elem = self.queue[0].pop(0)
        print('CONNECT {}'.format(elem))

    def check_qty_of_samples(self):
        self.sample_list = []
        for key, item in data.instances.items():
            if item.carried_by == 0 and item.status != 'researched':
                self.sample_list.append(item)

    def set_queue(self):
        #print( self.sample_list, file=sys.stderr)
        self.queue = []
        for sample in self.sample_list:
            queue_sample = []
            for elem, qty in sample.recipe.items():
                #print(elem, qty, file=sys.stderr)
                qty_required_in_queue = max(qty - self.stock[elem], 0)
                if qty_required_in_queue > 0:
                    queue_sample += [elem] * qty_required_in_queue
            self.queue.append(queue_sample)
        print(self.queue, file=sys.stderr)

    def explore_samples(self):
        print("CONNECT {}".format(2))  # pick the sample
        '''
        print("exploring samples", file=sys.stderr)
        max_rank_to_pick = 2
        max_health = 0
        sample_to_do = None
        print(data.instances.items(), file=sys.stderr)
        sorted_samples = dict(filter(lambda x: x.rank <= 2, data.instances.items()))
        print(sorted_samples, file=sys.stderr)

        for key, samples in data.instances.items():
            if samples.carried_by == -1 and samples.rank <= max_rank_to_pick:
                if samples.rank > max_health:
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
        '''
            
    def connect_to(self, module):
        print("CONNECT {}".format(module))
    
    def go_to(self, module):
        print("GOTO {}".format(module))
    
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
        
    available_a, available_b, available_c, available_d, available_e = [int(i) for i in input().split()]
    particle.liste['A'].stock = available_a
    particle.liste['B'].stock = available_b
    particle.liste['C'].stock = available_c
    particle.liste['D'].stock = available_d
    particle.liste['E'].stock = available_e

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

        this.carried_by = carried_by
        this.rank = rank
        this.health = health
        this.recipe['A'] = cost_a
        this.recipe['B'] = cost_b
        this.recipe['C'] = cost_c
        this.recipe['D'] = cost_d
        this.recipe['E'] = cost_e
        print(sample_id, carried_by, this.recipe, this.status, file=sys.stderr)
        
    if first_loop:
        me.first_move()
        first_loop = False
    else:
        me.next_move()
