import random
import math
import pyglet

class Individu:
    def __init__(self, P):
        self.path = P
        self.score = 0
        self.set_score()

    def set_score(self):
        for i in range(cities - 1):
            self.score += math.pow(self.path[i+1][0] - self.path[i][0], 2) + \
                          math.pow(self.path[i+1][1] - self.path[i][1], 2)

    def __repr__(self):
        return "{} - {}".format(self.path, self.score)

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


cities = 28
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
pts = []
inst = []

current = 0

if cities < 12:
    total = str(math.factorial(cities))
else:
    total = '{:.2e}'.format(math.factorial(cities))

window = pyglet.window.Window(width=w, height=h)

pyglet.gl.glPointSize(6)
pyglet.gl.glLineWidth(1)

@window.event
def on_draw():
    window.clear()
    for each in inst:
        pyglet.graphics.draw(2, pyglet.gl.GL_POINTS, ("v2i", each))

    best = population_list[0].path
    for i in range(cities - 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ("v2i", [best[i][0], best[i][1], best[i+1][0], best[i+1][1]]))

    label_total = pyglet.text.Label("Nombre de chemines existants : {}".format(total),
                              font_name='Times New Roman',
                              font_size=12,
                              color=(255, 255, 255, 255),
                              x=0, y=window.height,
                              anchor_x='left', anchor_y='top')

    label_tried = pyglet.text.Label("Nombre des chemins testés : {}".format(current),
                              font_name='Times New Roman',
                              font_size=12,
                              color=(255, 255, 255, 255),
                              x=0, y=window.height-15,
                              anchor_x='left', anchor_y='top')

    label_total.draw()
    label_tried.draw()

def update(df):
    global population_list, current

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

    current += len(new_indiv)
    population_list.extend(new_indiv)

for i in range(cities):
    pts.append(( random.randrange(10, w-10 ), random.randrange(10, h-10) ))

for i in range(cities-1):
    inst.append([pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1]])

for i in range(population):
    random.shuffle(pts)
    population_list.append(Individu(pts[:]))
current += population

pyglet.clock.schedule_interval(update, 1/20)
pyglet.app.run()
