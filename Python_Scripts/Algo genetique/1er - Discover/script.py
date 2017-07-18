import sys
import os
import random
import configparser
import time
import numpy as np

import matplotlib.pyplot as plt

def create_graphe():
    start_time = time.time()
    plt.figure(1)
    #plt.clf()
    plt.subplot(211)
    # x = np.linspace(X_MIN, X_MAX, 1000)
    x = np.arange(X_MIN, X_MAX, STEP)
    y = f(x)
    x2 = np.array([max(x) for x in echantillon.top])
    y2 = f(x2)
    x3 = np.array([min(x) for x in echantillon.top])
    y3 = f(x3)
    plt.plot(x, y, x2, y2,"rs",x3, y3, "gs")

    plt.subplot(212)

    for gen in echantillon.result.keys():
        x4 = echantillon.result[gen]
        y4 = gen*np.ones(len(x4))
        plt.plot(x4, y4, 'ro')

    print("Graph duration : ", time.time() - start_time)
    plt.show()

def randrange_float(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start

def f(x):
    y = np.sin(x/100)
    return y

def load_init():
    global X_MIN, X_MAX, POPULATION, RATIO_MUTATION, RATIO_CROISEMENT, RATIO_SELECTION, STEP, GENERATION
    config = configparser.ConfigParser()
    config.read([os.path.join(os.path.dirname(sys.argv[0]), 'setup.ini')])
    X_MIN = float(config.get('function', 'X_MIN'))
    X_MAX = float(config.get('function', 'X_MAX'))
    STEP = float(config.get('function', 'STEP'))
    POPULATION = int(config.get('algorithme', 'POPULATION'))
    GENERATION = int(config.get('algorithme', 'GENERATION'))
    RATIO_MUTATION = float(config.get('algorithme', 'RATIO_MUTATION'))
    RATIO_CROISEMENT = float(config.get('algorithme', 'RATIO_CROISEMENT'))
    RATIO_SELECTION = float(config.get('algorithme', 'RATIO_SELECTION'))
    """
    print("function:X_MIN=", X_MIN)
    print("function:X_MAX=", X_MAX)
    print("function:STEP=", STEP)
    print("algorithme:POPULATION=", POPULATION)
    print("algorithme:GENERATION=", GENERATION)
    print("algorithme:RATIO_MUTATION=", RATIO_MUTATION)
    print("algorithme:RATIO_CROISEMENT=", RATIO_CROISEMENT)
    print("algorithme:RATIO_SELECTION=", RATIO_SELECTION)
    """

class Individu():
    def __init__(self, num):
        self.ID = num
        self.individu = [0,0]
        self.score = 0

    def generate_me(self):
        self.individu = [randrange_float(X_MIN, X_MAX, STEP), randrange_float(X_MIN, X_MAX, STEP)]

    def muter(self):
        if random.random() > 0.5:
            self.individu[1] = randrange_float(X_MIN, X_MAX, STEP)
        else:
            self.individu[0] = randrange_float(X_MIN, X_MAX, STEP)
        self.set_score()

    def croiser(self, other_individu):
        new_elem = Individu(echantillon.index)
        new_elem.individu = [self.individu[0], other_individu.individu[1]]
        new_elem.set_score()
        echantillon.population.append(new_elem)
        echantillon.index +=1

    def set_score(self):
        self.score = abs(f(self.individu[0])-f(self.individu[1]))

class Population():
    def __init__(self):
        self.population = []
        self.result = {}
        self.top = []
        self.index = 0

    def set_population(self):
        while len(self.population) < POPULATION:
            elem = Individu(self.index)
            elem.generate_me()
            if elem.individu[0]!= elem.individu[1]:
                self.population.append(elem)
                elem.set_score()
                self.index += 1

    def set_ranking(self):
        self.population.sort(key=lambda x: x.score, reverse=True)

    def show(self, gen):
        print("")
        print(">>> GENERATION", gen, " <<<")
        print("")
        for each in self.population:
            print(each.ID, "-", each.score, ":", each.individu)

    def selectionne(self):
        seuil = int((1 - RATIO_SELECTION) * POPULATION)
        echantillon.population = echantillon.population[:seuil]

    def set_mutation(self):
        for each in self.population:
            if random.random() < RATIO_MUTATION:
                each.muter()

    def set_croisement(self):
        for each in self.population:
            if random.random() < RATIO_CROISEMENT:
                each.croiser(random.choice(self.population))

    def save_result(self, generation):
        self.result[generation] = [x.score for x in self.population]
        self.top.append(self.population[0].individu)

if __name__ == "__main__":
    start_time = time.time()
    load_init()

    #creation d'une population initiale (Generation 0):
    echantillon = Population()
    echantillon.set_population()

    #on les classe et on les affiche
    echantillon.set_ranking()

    #on save les resultat de la generation 0
    echantillon.save_result(0)
    #echantillon.show(0)

    #On modifie la generation au cours des generations
    for i in range(1, GENERATION):
        #on garde que les meilleurs en fonction du ratio de selection
        echantillon.selectionne()

        #on effectue les mutations
        echantillon.set_mutation()

        #on effectue les croisements
        echantillon.set_croisement()

        # on refais la population
        echantillon.set_population()

        #on tri par score chaque element:
        echantillon.set_ranking()

        #on sauvegarde les resultats de la generation i pour le graphe
        echantillon.save_result(i)

        #on montre le resultat
        #echantillon.show(i)

    print("Script duration : ", time.time()-start_time)
    create_graphe()