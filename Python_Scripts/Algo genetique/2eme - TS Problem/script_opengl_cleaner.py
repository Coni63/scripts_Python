import random
import math
import pyglet
import configparser

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
    def __init__(self, algo_setting, pb_setting):
        self.number_of_cities = pb_setting["number_of_cities"]
        self.mutation_ratio = algo_setting["mutation"]
        self.cross_ratio = algo_setting["crossover"]
        self.population = algo_setting["population_count"]
        self.population_list = []
        self.pts_list = []
        self.vertices = []
        self.current = 0

        for i in range(self.number_of_cities):
            w = algo_setting["width"]
            h = algo_setting["height"]
            b = algo_setting["border"]
            self.pts_list.append((random.randrange(b, w-b ), random.randrange(b, h-b )))

        for i in range(self.number_of_cities - 1):
            self.vertices.append([self.pts_list[i][0], self.pts_list[i][1], self.pts_list[i + 1][0], self.pts_list[i + 1][1]])

        if self.number_of_cities < 12:
            self.total = str(math.factorial(self.number_of_cities))
        else:
            self.total = '{:.2e}'.format(math.factorial(self.number_of_cities))

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


class MyWindow(pyglet.window.Window):
    def __init__(self, windows_settings):
        super(MyWindow, self).__init__(**windows_settings)
        self.set_minimum_size(400, 300)
        pyglet.gl.glPointSize(6)
        pyglet.gl.glLineWidth(1)
        self.best_ind = pop.best_individu
        self.tried = 0

    def on_draw(self):
        self.clear()
        for vertex in pop.vertices:
            pyglet.graphics.draw(2, pyglet.gl.GL_POINTS, ("v2i", vertex))

        best = self.best_ind.path
        for i in range(pop.number_of_cities - 1):
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ("v2i", [best[i][0], best[i][1], best[i+1][0], best[i+1][1]]))

        label_total = pyglet.text.Label("Nombre de chemins existants : {}".format(pop.total),
                                        font_name='Times New Roman',
                                        font_size=12,
                                        color=(255, 255, 255, 255),
                                        x=0, y=self.height,
                                        anchor_x='left', anchor_y='top')

        label_tried = pyglet.text.Label("Nombre des chemins testés : {}".format(self.tried),
                                        font_name='Times New Roman',
                                        font_size=12,
                                        color=(255, 255, 255, 255),
                                        x=0, y=self.height - 15,
                                        anchor_x='left', anchor_y='top')
        label_total.draw()
        label_tried.draw()

    def update(self, df):
        pop.evolve()
        self.best_ind = pop.best_individu
        self.tried = pop.current


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("setting.ini")
    setup_window = {
            "width": config.getint('UI', 'width'),
            "height": config.getint('UI', 'height'),
            "resizable":config.getboolean('UI', 'resizable'),
            "caption": config.get('UI', 'title')
    }

    setup_population = {
        "population_count" : config.getint('IA', 'population_size'),
        "mutation": config.getfloat('IA', 'mutation_rate'),
        "crossover": config.getfloat('IA', 'crossover_rate'),
        "width": config.getint('UI', 'width'),
        "height": config.getint('UI', 'height'),
        "border" : config.getint('UI', 'border')
    }
    settings = {
        "number_of_cities" : config.getint('PB', 'node_count')
    }

    pop = Population(setup_population, settings, )
    window = MyWindow(setup_window)
    pyglet.clock.schedule_interval(window.update, 1 / 24)
    pyglet.app.run()


