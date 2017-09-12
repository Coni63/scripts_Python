# import random
# import math
#
# class Individu:
#     def __init__(self, P):
#         self.path = P
#         self.score = 0
#         self.set_score()
#         self.fitness = 0
#
#     def set_score(self):
#         for i in range(cities - 1):
#             self.score += math.pow(self.path[i+1][0] - self.path[i][0], 2) + \
#                           math.pow(self.path[i+1][1] - self.path[i][1], 2)
#
#     def __repr__(self):
#         return "{} - {}".format(self.path, self.fitness)
#
#     def mutate(self):
#         a = random.randrange(cities)
#         b = random.randrange(cities)
#         new_path = self.path[:]
#         new_path[a], new_path[b] = new_path[b], new_path[a]
#         return [Individu(new_path)]
#
#     def cross_over(self, other):
#         a = random.randrange(cities)
#         b = random.randrange(cities)
#         if a != b :
#             start = min(a, b)
#             end = max(a, b)
#         else:
#             start = 0
#             end = cities // 2
#
#         new1 = self.path[start:end]
#         new2 = self.path[:start] + self.path[end:]
#         for each in other.path:
#             if each not in new1:
#                 new1 += [each]
#         for each in self.path:
#             if each not in new2:
#                 new2 += [each]
#
#         return [Individu(new1), Individu(new2)]
#
#
# cities = 35
# w, h = 800, 600
#
#
# #define genetic parameter
# mutation_ratio = 5e-1
# cross_ratio = 0.7
# population = 100
# population_list = []
#
# best_every_gen = []
#
# pts = []
# for i in range(cities):
#     pts.append(( random.randrange(w), random.randrange(h) ))
#
# for i in range(population):
#     random.shuffle(pts)
#     population_list.append(Individu(pts[:]))
#
# while True:
#     population_list.sort(key = lambda x : x.score)
#     to_delete = population_list[population//2:]
#     population_list = population_list[:population//2]
#
#     # Delete all instances not kept to free memory
#     for each in to_delete:
#         del each
#
#     print(to_delete)
#
#     break
#
#     new_indiv = []
#     for elem in population_list:
#         if random.random() < cross_ratio and len(new_indiv) < population//2:
#             elem2 = random.choice(population_list)
#             while elem == elem2:
#                 elem = random.choice(population_list)
#             new_indiv += elem.cross_over(elem2)
#
#     # mutation
#     for each in population_list:
#         if random.random() <= mutation_ratio:
#             new_indiv += each.mutate()
#
#     population_list.extend(new_indiv)
#
#     print(population_list[0].score)
#     best_every_gen.append(population_list[0])


import random
import math

class Individu:
    def __init__(self, P):
        self.path = P
        self.score = 0
        self.set_score()
        self.fitness = 0

    def set_score(self):
        for i in range(len(self.path) - 1):
            self.score += math.pow(self.path[i+1][0] - self.path[i][0], 2) + \
                          math.pow(self.path[i+1][1] - self.path[i][1], 2)

    def __repr__(self):
        return "{} - {}".format(self.path, self.fitness)

    def mutate(self):
        a = random.randrange(len(self.path))
        b = random.randrange(len(self.path))
        new_path = self.path[:]
        new_path[a], new_path[b] = new_path[b], new_path[a]
        return [Individu(new_path)]

    def cross_over(self, other):
        a = random.randrange(len(self.path))
        b = random.randrange(len(self.path))
        if a != b :
            start = min(a, b)
            end = max(a, b)
        else:
            start = 0
            end = len(self.path) // 2

        new1 = self.path[start:end]
        new2 = self.path[:start] + self.path[end:]
        for each in other.path:
            if each not in new1:
                new1 += [each]
        for each in self.path:
            if each not in new2:
                new2 += [each]

        return [Individu(new1), Individu(new2)]

nb_cities = 35
best_every_gen = []
w, h = 1000, 1000 #space for cities

#define genetic parameter
mutation_ratio = 5e-1
cross_ratio = 0.7
population = 100
population_list = []

# cities = []
# for i in range(nb_cities):
#     cities.append(( random.randrange(w), random.randrange(h) ))
# cities = [( random.randrange(w), random.randrange(h) )]
# print(cities)

cities = [( random.randrange(w), random.randrange(h) ) for _ in range(nb_cities)]

for i in range(population):
    random.shuffle(cities)
    population_list.append(Individu(cities[:]))

improvement = 0
previous_best = 1e20
max_generation = 10000
current_generation = 0

while current_generation < max_generation and improvement < 100:
    # ranking
    population_list.sort(key=lambda x: x.score)

    # Selection
    to_delete = population_list[population // 2:]
    population_list = population_list[:population // 2]

    # Delete all instances not kept to free memory
    to_delete.clear()

    # For each remaining elements, we do crossover
    new_indiv = []
    for elem in population_list:
        if random.random() < cross_ratio and len(new_indiv) < population // 2:
            elem2 = random.choice(population_list)
            while elem == elem2:
                elem = random.choice(population_list)
            new_indiv += elem.cross_over(elem2)

    # and mutation
    for each in population_list:
        if random.random() <= mutation_ratio:
            new_indiv += each.mutate()

    population_list.extend(new_indiv)

    best_this_generation = population_list[0].score
    #print(best_this_generation)
    if best_this_generation < previous_best:
        previous_best = best_this_generation
        improvement += 1
        best_every_gen.append((current_generation, population_list[0]))
        print(current_generation, best_this_generation)

    current_generation += 1