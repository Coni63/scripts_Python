import random
import math
import configparser
import vpython


class Individu:
    def __init__(self, P):
        self.path = P
        self.score = 0
        self.set_score()
        self.fitness = 0

    def set_score(self):
        for i in range(len(self.path) - 1):
            self.score += math.pow(self.path[i+1][0] - self.path[i][0], 2) + \
                          math.pow(self.path[i+1][1] - self.path[i][1], 2) + \
                          math.pow(self.path[i+1][2] - self.path[i][2], 2)

    def __repr__(self):
        return "{} - {}".format(self.path, self.fitness)

    def mutate(self):
        a = random.randrange(pop.number_of_cities)
        b = random.randrange(pop.number_of_cities)
        new_path = self.path[:]
        new_path[a], new_path[b] = new_path[b], new_path[a]
        return [Individu(new_path)]

    def cross_over(self, other):
        a = random.randrange(pop.number_of_cities)
        b = random.randrange(pop.number_of_cities)
        if a != b :
            start = min(a, b)
            end = max(a, b)
        else:
            start = 0
            end = pop.number_of_cities // 2

        new1 = self.path[start:end]
        new2 = self.path[:start] + self.path[end:]
        for each in other.path:
            if each not in new1:
                new1 += [each]
        for each in self.path:
            if each not in new2:
                new2 += [each]

        return [Individu(new1), Individu(new2)]


class Population:
    def __init__(self, params):
        self.number_of_cities = params["nb_cities"]
        self.mutation_ratio = 0.05
        self.cross_ratio = 0.5
        self.population = 100
        self.population_list = []
        self.pts_list = []
        self.vertices = []
        self.current = 0
        self.width = params["width"]
        self.height = params["height"]
        self.depth = params["depth"]

        for i in range(self.number_of_cities):
            self.pts_list.append( [ random.randrange(0, self.width), random.randrange(0, self.width), random.randrange(0, self.width) ] )

        for i in range(self.number_of_cities - 1):
            self.vertices.append([self.pts_list[i][0], self.pts_list[i][1], self.pts_list[i][2], self.pts_list[i + 1][0], self.pts_list[i + 1][1], self.pts_list[i+1][2]])

        if self.number_of_cities < 12:
            self.total = str(math.factorial(self.number_of_cities))
        elif self.number_of_cities < 70:
            self.total = '{:.2e}'.format(math.factorial(self.number_of_cities))
        else:
            self.total = "Infinity"

        self.create_init_population()
        self.best_individu = min(self.population_list, key=lambda x:x.score)

    def create_init_population(self):
        for i in range(self.population):
            random.shuffle(self.pts_list)
            self.population_list.append(Individu(self.pts_list[:]))
        self.current += self.population

    def evolve(self):
        self.population_list.sort(key=lambda x: x.score)
        to_delete = self.population_list[self.population//2:]
        population_list = self.population_list[:self.population//2]

        self.best_individu = population_list[0]

        # Delete all instances not kept to free memory
        to_delete.clear()

        new_indiv = []
        # croisement
        for elem in population_list:
            if random.random() < self.cross_ratio and len(new_indiv) < self.population//2:
                elem2 = random.choice(self.population_list)
                while elem == elem2:
                    elem = random.choice(self.population_list)
                new_indiv += elem.cross_over(elem2)

        # mutation
        for each in population_list:
            if random.random() <= self.mutation_ratio:
                new_indiv += each.mutate()

        self.current += len(new_indiv)
        self.population_list.extend(new_indiv)

    def run(self):
        while True:
            self.evolve()
            print("current_best ",self.best_individu.score)


def change():  # Appelé par controls quand on clique sur le bouton
    if b.text == 'Click me':
        b.text = 'Try again'
    else:
        b.text = 'Click me'

def render(pop, params):

    v_scene = params["width"] * params["height"] * params["depth"]
    r = math.floor(((3 * v_scene)/(100*4*3.14*params["nb_cities"]))**(1/3))
    t = r / 5

    scene = vpython.scene
    scene.center = vpython.vector(params["width"]//2, params["height"]//2, params["depth"]//2)
    scene.width = params["width"]
    scene.height = params["height"]

    for city in pop.pts_list:
        vpython.sphere(pos=vpython.vector(*city), radius=r, color=vpython.color.green)

    pop.evolve()
    path = pop.best_individu.path
    p = vpython.curve(pos=path, radius=t)

    while True:
        vpython.rate(10)
        pop.evolve()
        path = pop.best_individu.path
        p.clear()
        p.append(path)


if __name__ == "__main__":
    parameters = {
        "width":1200,
        "height":800,
        "depth":800,
        "nb_cities":50
    }
    pop = Population(parameters)
    render(pop, parameters)

