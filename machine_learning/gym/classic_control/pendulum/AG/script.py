import math
import random
from math import pi
import sys
import pickle
import numpy as np
import gym


def trigo_to_angle(env):
    cos, sin = env[0], env[1]
    a = math.acos(cos)
    # b = math.asin(sin)
    # l1 = [2 * pi + a, 2 * pi - a]
    # l2 = [(2 * pi) + b, (3 * pi - b)]
    # for x in l1:
    #     for y in l2:
    #         if abs(x % (2 * pi) - y % (2 * pi)) < 0.001:
    #             # print(math.degrees(x%(2*pi)))
    #             return x % (2 * pi)
    if sin < 0:
        return -a
    else:
        return a


class Individu:
    def __init__(self, param):
        self.genome = param
        self.score = 0
        self.fitness = 0

    def __repr__(self):
        return "{} \t- > {}".format(self.genome, self.score)

    def activation(self, env, prev_error, sum_error):
        P, I, D = self.genome
        cos_theta, sin_theta, theta_point = env
        theta = trigo_to_angle(env)
        error = theta
        sum_error += error
        s = P*error + I*(sum_error) + D*(error-prev_error)
        return s, error, sum_error

    def calculate_fitness(self):
        self.fitness = 2/(1+math.exp(-self.score/100))
        return self.fitness

    def mutate(self):
        pos = random.randint(0, 2)
        percent_max = 10
        factor = 1 + random.random()/percent_max - 1/(2*percent_max)
        new_genome = self.genome[:]
        new_genome[pos] *= factor
        return Individu(new_genome)

    def cross(self, other):
        split = random.randint(0, 2)
        genome_a = self.genome[:]
        genome_b = other.genome[:]
        genome_a[split], genome_b[split] = genome_b[split], genome_a[split]
        return [Individu(genome_a), Individu(genome_b)]

class Population:
    def __init__(self, size=50):
        self.size = size
        self.selection_rate = 0.5
        self.mutation_rate = 0.05
        self.crossover_rate = 0.25
        self.min = -10
        self.max = 10
        self.population = []

    def generate_population(self):
        req = max(0, self.size - len(self.population))
        for _ in range(self.size - len(self.population)):
            genome = [((random.random() * (self.max - self.min)) + self.min) for _ in range(3)]
            self.population.append(Individu(genome))


if __name__ == "__main__":
    env = gym.make("Pendulum-v0")

    pop = Population(size=100)
    pop.generate_population()

    for each in pop.population:
        print(each)

    obs_gen = env.reset()[:]
    for generation in range(100):
        print("###########  GENERATION {} ##########".format(generation))
        # Evaluation
        for indiv in pop.population:
            sum_error = 0
            score = 0
            error = 0
            loop = 0
            obs = obs_gen
            while loop < 150:
                # env.render()
                action, error, sum_error = indiv.activation(obs, error, sum_error)
                obs, reward, done, info = env.step([action])
                score += reward
                loop += 1
            indiv.score = score
            #print(indiv)

        new_indiv = []

        # Selection
        #pop.population = sorted(pop.population, key=lambda x:x.score, reverse=True)
        w = [x.calculate_fitness() for x in pop.population]
        threshold = math.floor(pop.selection_rate * len(pop.population))
        #pop.population = pop.population[:threshold]
        pop.population = random.choices(pop.population, weights=w, k=threshold)

        # Crossover
        w = [x.calculate_fitness() for x in pop.population]
        threshold = 2*(math.floor(pop.crossover_rate * len(pop.population))//2)
        sample = random.choices(pop.population, weights=w, k=threshold)
        for i in range(threshold//2):
            new_indiv.extend(sample[i].cross(sample[-i]))

        # mutation
        for indiv in pop.population:
            if random.random() < pop.mutation_rate:
                new_indiv.append(indiv.mutate())

        # merge
        pop.population.extend(new_indiv)
        pop.generate_population() # rempli a sa pop max avec des indiv random

        print("Best this generation => {}".format(pop.population[0]))
        print("Number of Indiv => {}".format(len(pop.population)))

    best = pop.population[0]
    # best = Individu([8.519574012334918, -1.836529289909322, -0.12871889470149966]) #
    error = 0
    sum_error = 0
    obs = env.reset()
    while True:
        env.render()
        #print(obs)
        action, error, sum_error = best.activation(obs, error, sum_error)
        obs, reward, done, info = env.step([action])
        if done:
            break
