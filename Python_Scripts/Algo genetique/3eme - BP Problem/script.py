import random
import math
import pyglet
import configparser
import copy
import numpy as np

# class Objet:
#     instances = []
#     def __init__(self, id, weight, price, volume):
#         self.ID = id
#         self.weight = weight
#         self.price = price
#         self.volume = volume
#         self.instances.append(self)
#
#     def __repr__(self):
#         return "item {} : M = {}g, V = {:.2f}L, P = {}€".format(self.ID, self.weight, self.volume, self.price)
#
# class BackPack:
#     def __init__(self, V, W, liste_item):
#         self.MAX_VOLUME = V
#         self.MAX_WEIGHT = W
#         self.weight = 0
#         self.price = 0
#         self.volume = 0
#         self.inside = []
#         self.outside = liste_item
#
#     def remplir(self):
#         random.shuffle(self.outside)
#         for item in self.outside:
#             if self.weight + item.weight < self.MAX_WEIGHT and self.volume + item.volume < self.MAX_VOLUME:
#                 self.outside.remove(item)
#                 self.inside.append(item)
#                 self.weight += item.weight
#                 self.volume += item.volume
#                 self.price += item.price
#
#     def __repr__(self):
#         return "M = {}/{} , V = {}/{}, P = {}".format(self.weight, self.MAX_WEIGHT, self.volume, self.MAX_VOLUME, self.price)
#
#     def mutate(self):
#         removed_item = random.choice(self.inside)
#         self.inside.remove(removed_item)
#         self.weight -= removed_item.weight
#         self.volume -= removed_item.volume
#         self.price -= removed_item.price
#         random.shuffle(self.outside)
#         for item in self.outside:
#             if self.weight + item.weight < self.MAX_WEIGHT and self.volume + item.volume < self.MAX_VOLUME:
#                 self.outside.remove(item)
#                 self.inside.append(item)
#                 self.weight += item.weight
#                 self.volume += item.volume
#                 self.price += item.price
#                 break
#         self.outside.append(removed_item)
#
# if __name__ == "__main__":
#     config = configparser.ConfigParser()
#     config.read("setting.ini")
#     # setup_window = {
#     #         "width": config.getint('UI', 'width'),
#     #         "height": config.getint('UI', 'height'),
#     #         "resizable":config.getboolean('UI', 'resizable'),
#     #         "caption": config.get('UI', 'title')
#     # }
#
#     setup_population = {
#         "population_count" : config.getint('IA', 'population_size'),
#         "mutation": config.getfloat('IA', 'mutation_rate'),
#         "crossover": config.getfloat('IA', 'crossover_rate'),
#         "width": config.getint('UI', 'width'),
#         "height": config.getint('UI', 'height'),
#         "border" : config.getint('UI', 'border')
#     }
#     settings = {
#         "number_of_cities" : config.getint('PB', 'node_count')
#     }

    # pop = Population(setup_population, settings )
    # window = MyWindow(setup_window)

    # for i in range(100):
    #     w = random.randint(1, 5000) #masse en g
    #     v = random.random()*30+1 #volume en L
    #     p = random.randint(1, 500) #prix en €
    #     Objet(i, w, p, v)

    # bp_instances = []
    # for i in range(100):
    #     bp = BackPack(50, 20000, Objet.instances[:])
    #     bp.remplir()
    #     bp_instances.append(bp)
    #
    # # evaluate
    # bp_instances.sort(key = lambda x:x.price, reverse=True)
    #
    # # selection
    # to_delete = bp_instances[50:]
    # bp_instances = bp_instances[:50]
    # for item in to_delete:
    #     del item
    #
    # # mutation
    # for backpack in bp_instances:
    #     if random.random() < 0.05:
    #         new_backpack = copy.deepcopy(backpack)
    #         new_backpack.mutate()
    #         bp_instances.append(new_backpack)
    #
    # #crossover

number_of_items = 5
w = np.random.rand(number_of_items) * 5000
v = np.random.rand(number_of_items) * 30
p = np.random.rand(number_of_items) * 500

backpack_volume = sum(v)//2
backpack_weight = sum(w)//2

# generation de la population
population = 100
pop = np.random.randint(0, 2 , size=(population, number_of_items))

nb_generation = 100
for generation in range(nb_generation):
    # evaluation
    total_mass = np.matmul(pop, w)
    total_volume = np.matmul(pop, v)
    total_value = np.matmul(pop, p)

    for i in range(population):
        if total_mass[i] > backpack_weight:
            total_value[i] /= 2
        if total_volume[i] > backpack_volume:
            total_value[i] /= 2

    print(total_value)

    maxi = max(total_value)
    fitness = total_value/maxi
    improved_fitness = fitness + np.random.rand(population)

    idx = np.argsort(improved_fitness, axis=0)[::-1]

    pop = pop[idx]
    total_mass = total_mass[idx]
    total_volume = total_volume[idx]
    total_value = total_value[idx]
    improved_fitness = improved_fitness[idx]

    # selection
    median = np.median(improved_fitness)

    to_delete = (improved_fitness < median)

    pop = pop[to_delete == False]
    total_mass = total_mass[to_delete == False]
    total_volume = total_volume[to_delete == False]
    total_value = total_value[to_delete == False]
    improved_fitness = improved_fitness[to_delete == False]

    # crossover



