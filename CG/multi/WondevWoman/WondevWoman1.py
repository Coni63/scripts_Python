import sys
import math
#import pandas as pd
#import numpy as np
#import random
import time.time

size = int(input())
units_per_player = int(input())

carte = []

class Cell:
    cell_pos = {}
    def __init__(self, character, x, y):
        self.x = x
        self.y = y
        if character == '.':
            self.sol = False
            self.height = '.'
        else:
            self.sol = True
            self.height = int(character)
        self.busy = False
        self.cell_pos[(self.x, self.y)] = self

    def __repr__(self):
        return "{}".format(self.height)

    def set_free(self):
        self.busy = False
        self.team = None
    
    def set_busy(self, T):
        self.busy = True
        self.team = T

class Perso:
    instances = {}
    def __init__(self, T, x, y):
        self.ID = len(self.instances)
        self.x = x
        self.y = y
        self.team = T
        self.instances[self.ID] = self

    def __repr__(self):
        if self.team == 1:
            return "Allié ({},{})".format(self.x, self.y)
        else:
            return "Enemy ({},{})".format(self.x, self.y)
    

# game loop
first_lap = True
while True:
    for i in range(size):
        row = list(input())
        line = []
        for index, cell in enumerate(row):
            line.append(Cell(cell, index, i))
        carte.append(line)
        print(line, file=sys.stderr)
    width = len(row)

    count = 0
    for i in range(units_per_player):
        unit_x, unit_y = [int(j) for j in input().split()]
        Cell.cell_pos[(unit_x, unit_y)].set_busy(1)
        if count not in Perso.instances.keys():
            Perso(1, unit_x, unit_y)
        else:
            Perso.instances[count].x = unit_x
            Perso.instances[count].y = unit_y
        count += 1 

    for i in range(units_per_player):
        other_x, other_y = [int(j) for j in input().split()]
        Cell.cell_pos[(unit_x, unit_y)].set_busy(-1)
        if count not in Perso.instances.keys():
            Perso(-1, unit_x, unit_y)
        else:
            Perso.instances[count].x = unit_x
            Perso.instances[count].y = unit_y
        count += 1 
    
    #print(Perso.instances, file=sys.stderr)

    #arr = []
    legal_actions = int(input())
    for i in range(legal_actions):
        atype, index, dir_1, dir_2 = input().split()
        index = int(index)
        heros = Perso.instances[index]
        #arr.append([atype, index, dir_1, dir_2])

        # gestion du move
        if dir_1 == "N" and heros.y > 0:
            if carte[heros.y - 1][heros.x] in range(0, carte[heros.y][heros.x] + 2):
                level = carte[heros.y - 1][heros.x]

        elif dir_1 == "NE" and heros.y > 0 and heros.x < width - 1 :
            if carte[heros.y - 1][heros.x + 1] in range(0, carte[heros.y][heros.x] + 2):
                level = carte[heros.y - 1][heros.x + 1]

        elif dir_1 == "E" and heros.x < width - 1:
            if carte[heros.y][heros.x + 1] in range(0, carte[heros.y][heros.x] + 2):
                level = carte[heros.y][heros.x + 1]

        elif dir_1 == "SE" and heros.y < size - 1 and heros.x < width - 1 :
            if carte[heros.y + 1][heros.x] in range(0, carte[heros.y][heros.x] + 2):
                level = carte[heros.y + 1][heros.x]

        elif dir_1 == "S" and heros.y < size - 1 :
            if carte[heros.y + 1][heros.x] in range(0, carte[heros.y][heros.x] + 2):
                level = carte[heros.y + 1][heros.x]

        elif dir_1 == "SW" and heros.x > 0 and heros.y < size - 1:
            if carte[heros.y + 1][heros.x - 1] in range(0, carte[heros.y][heros.x] + 2):
                level = carte[heros.y + 1][heros.x - 1]

        elif dir_1 == "W" and heros.x > 0:
            if carte[heros.y][heros.x - 1] in range(0, carte[heros.y][heros.x] + 2):
                level = carte[heros.y][heros.x - 1]

        elif dir_1 == "NW" and heros.y > 0 and heros.x > 0:
            if carte[heros.y - 1][heros.x - 1] in range(0, carte[heros.y][heros.x] + 2):
                level = carte[heros.y - 1][heros.x - 1]

        # gestion du build
        if dir_2 == "N":

        elif dir_2 == "NE":

        elif dir_2 == "E":

        elif dir_2 == "SE":

        elif dir_2 == "S":

        elif dir_2 == "SW":

        elif dir_2 == "W":

        elif dir_2 == "NW":

    #choix = pd.DataFrame(arr, columns=[ 'type', 'index', 'dir1', 'dir2' ])
    #print(choix, file=sys.stderr)

    print("MOVE&BUILD 0 N S")