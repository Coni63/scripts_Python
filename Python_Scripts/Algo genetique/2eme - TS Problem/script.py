import pygame
import random
import math
import pyglet

class Individu:
    def __init__(self, P):
        self.path = P
        self.score = 0
        self.set_score()
        self.fitness = 0

    def set_score(self):
        for i in range(cities - 1):
            self.score += math.pow(self.path[i+1][0] - self.path[i][0], 2) + \
                          math.pow(self.path[i+1][1] - self.path[i][1], 2)

    def __repr__(self):
        return "{} - {}".format(self.path, self.fitness)

    def mutate(self):
        a = random.randrange(cities)
        b = random.randrange(cities)
        new_path = self.path[:]
        new_path[a], new_path[b] = new_path[b], new_path[a]
        return [Individu(new_path)]

    def cross_over(self, other):
        a = random.randrange(cities)
        b = random.randrange(cities)
        if a != b :
            start = min(a, b)
            end = max(a, b)
        else:
            start = 0
            end = cities // 2

        new1 = self.path[start:end]
        new2 = self.path[:start] + self.path[end:]
        for each in other.path:
            if each not in new1:
                new1 += [each]
        for each in self.path:
            if each not in new2:
                new2 += [each]

        return [Individu(new1), Individu(new2)]


cities = 35
w, h = 800, 600
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#define genetic parameter
mutation_ratio = 5e-1
cross_ratio = 0.7
population = 100
population_list = []

best_every_gen = []

# pygame.init()
# fenetre = pygame.display.set_mode((w, h))

def on_draw():
    window.clear()
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
                         ('v2f', (10, 15, 30, 35))
                         )

window = pyglet.window.Window()

pts = []
for i in range(cities):
    pts.append(( random.randrange(w), random.randrange(h) ))

for i in range(population):
    random.shuffle(pts)
    population_list.append(Individu(pts[:]))

print(population_list[0].score)

while True:
    population_list.sort(key = lambda x : x.score)
    to_delete = population_list[population//2:]
    population_list = population_list[:population//2]

    # Delete all instances not kept to free memory
    for each in to_delete:
        del each

    new_indiv = []
    # croisement
    for elem in population_list:
        if random.random() < cross_ratio and len(new_indiv) < population//2:
            elem2 = random.choice(population_list)
            while elem == elem2:
                elem = random.choice(population_list)
            new_indiv += elem.cross_over(elem2)

    # mutation
    for each in population_list:
        if random.random() <= mutation_ratio:
            new_indiv += each.mutate()

    population_list.extend(new_indiv)

    print(population_list[0].score)
    best_every_gen.append(population_list[0])

    # fenetre.fill(0)
    #
    # for pt in pts:
    #     pygame.draw.circle(fenetre, WHITE, pt, 3)
    #
    # pygame.draw.lines(fenetre, GREEN, False, population_list[0].path, 2)
    #
    # pygame.display.flip()
    # pygame.time.wait(500)

