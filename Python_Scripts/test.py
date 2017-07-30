# import gc
#
# #gc.enable()
#
# a = 2
# collected = gc.collect()
# b = 4
# collected = gc.collect()
#
# print("Garbage collector: collected %d objects." % (collected))

# import numpy as np
#
# a = np.zeros((10, 9, 5))
# b = np.ones((10, 9, 5))
#
# print('---avant---')
# print('a x', a[:, 0, 0])
# print('a y', a[0, :, 0])
# print('a z', a[0, 0, :])
#
# #for i in range(0, 10):
# #a[:5, 0:0, 0:0] = b[:5, 0:0, 0:0]
#
# i, j, k = 5, 1 ,2
# a[:,0,0][:i] = b[:,0,0][:i]
# a[0,:,0][:j] = b[0,:,0][:j]
# a[0,0,:][:k] = b[0,0,:][:k]
#
# print('---après---')
# print('a x', a[:, 0, 0])
# print('a y', a[0, :, 0])
# print('a z', a[0, 0, :])
#
# import timeit
#
# def f(i):
#     return arr[i]
#
# def g(i):
#     return dico[i]
#
# t = "abcdefghijklmnopqrstuvwxyz"
# arr = list(t)
# dico = {}
# for i, l in enumerate(t):
#     dico[i] = l
# print(arr)
# print(dico)
#
# print(timeit.timeit("f(5)", setup="from __main__ import f",  number=10000))
# print(timeit.timeit("g(5)", setup="from __main__ import g",  number=10000))

# a =[3, 1, 2]
# b = a
# b.sort()
# print(b)
# print(a)

# a = [1, 2]
# b = [2, 3]
# print(set(a) & set(b))

# import random
# import string
# import time
#
# def generate_string(l):
#     return "".join([ random.choice(string.ascii_letters) for _ in range(l)])
#
# group_short = {}
# group_long = {}
#
# for i in range(5000):
#     group_short[i] = generate_string(5)
#
# for i in range(500000):
#     group_long[i] = generate_string(5)
#
# t_short = time.time()
# for i in range(0, 5000):
#     del group_short[i]
# print(time.time()-t_short)
#
# t_long = time.time()
# for j in range(0, 150000, 30):
#     del group_long[j]
# print(time.time()-t_long)

# import scipy.linalg
#
# A = scipy.linalg.circulant(8)
# print(A)

# import pandas as pd
# import numpy as np
#
# df3 = pd.DataFrame(np.random.randn(8, 3), columns= ['M', 'N', 'O'])
# df4 = pd.DataFrame(np.random.randn(8, 3), columns= ['M', 'N', 'O'])
# df5 = pd.DataFrame(np.random.randn(8, 3), columns= ['M', 'N', 'O'])
#
# df = pd.concat([df3, df4, df5])
# print(df.mean())


# a = [1, 8, 2, 4]
# b = a[:]
# c = a[:]
#
# a = [x/max(a) for x in a]
# print(a)
#
# for i in range(4):
#     b[i] /= max(b)
# print(b)
#
# for x in c:
#     x = x/max(c)
# print(c)

# import math
#
#
# def convertion_binaire(nb_entier):  # fonction qui convertit un nombre entier en binaire<br>
#     code_binaire = []
#     x = nb_entier
#     q = int(x / 2)
#     r = x - 2 * q
#     code_binaire.append(r)
#
#     while q > 0:
#         x = q
#         q = int(x / 2)
#         r = x - 2 * q
#         code_binaire.append(r)
#
#     code_binaire.reverse()
#     print("Le code binaire de " + str(nb_entier) + " est :")
#     print(code_binaire)
#     return code_binaire
#
#
# a = 2.751
#
# if int(a) < 0:  # on verifie si le nombre est negatif#
#     a = abs(a)
#     S = 1
# else:
#     S = 0
#
# part_entiere = int(str(a).split(".")[0])
# part_decimale = int(str(a).split(".")[1])
#
# code_part_ent = convertion_binaire(part_entiere)
# code_part_dec = convertion_binaire(part_decimale)

# import time
#
# a = 2.571
#
# a = str(a)
# start = time.time()
# for i in range(100000):
#     a_s = a.split(".")
#     part_entiere = int(a_s[0])
#     part_decimale = int(a_s[1])
# print(time.time() - start)
#
# start = time.time()
# for i in range(100000):
#     x, y = a.split('.')
#     entier, decimal = int(x), int(y)
# print(time.time() - start)
#
# start = time.time()
# for i in range(100000):
#     i = a.find('.')
#     entier, decimal = int(a[:i]), int(a[i + 1:])
# print(time.time() - start)

# start = time.time()
# for i in range(100000):
#     part_entiere = int(str(a).split(".")[0])
#     part_decimale = int(str(a).split(".")[1])
# print(time.time() - start)
#
# start = time.time()
# for i in range(100000):
#     x, y = str(a).split('.')
#     entier, decimal = int(x), int(y)
# print(time.time() - start)
#
# start = time.time()
# for i in range(100000):
#     i = str(a).find('.')
#     entier, decimal = int(str(a)[:i]), int(str(a)[i + 1:])
# print(time.time() - start)

#
# def printOne(name, goal1):
#     score1 = []
#     for i in range(len(name)):
#         print("\t\t\t\t" + name[i] + "\t " + str(point[i]) + " point - \t" + str(goal1[i]) + " buts")
#
#         score1.append(point[i])
#
#     print(score1)
#
#
# name = ["Henry", "Owen", "Drogba"];
# point = [2, 4, 6]
# goal1 = [18, 12, 6]
# goal2 = [6, 8, 5]
#
# #printOne(name, goal1)
# score_per_player = dict(zip(name, point))
# print(score_per_player)
#
# goal_per_player = list(zip(name, goal1))
# goal_per_player.sort(key=lambda x:x[1])
#
# for index, player_info in enumerate(goal_per_player):
#     score_per_player[player_info[0]] += point[index]
#
# print(score_per_player)
#
# def tris(name, goal1, goal2):
#     for i in range(len(name) - 1, 0, -1):
#         for j in range(i):
#             if name[j + 1] < name[j]:
#                 tempoName = name[j]
#                 tempoGoal1 = goal1[j]
#                 tempoGoal2 = goal2[j]
#                 name[j] = name[j + 1]
#                 goal1[j] = goal1[j + 1]
#                 goal2[j] = goal2[j + 1]
#                 name[j + 1] = tempoName
#                 goal1[j + 1] = tempoGoal1
#                 goal2[j + 1] = tempoGoal2
#
#
# def trier(joueur, goal, goal2, point):
#     swap = True
#     while swap:
#         swap = False
#         for i in range(len(joueur)-1):
#             if goal[i+1] > goal[i]:
#                 joueur[i], joueur[i+1] = joueur[i+1], joueur[i]
#                 goal[i], goal[i+1] = goal[i+1], goal[i]
#                 goal2[i], goal2[i+1] = goal2[i+1], goal2[i]
#                 point[i], point[i + 1] = point[i + 1], point[i]
#                 swap = True
#     return joueur, goal, goal2, point
#
#
# def printOne(name, goal1, goal2):
#     score1 = []
#     score2 = []
#     but1 = []
#     but2 = []
#     for i in range(len(name)):
#         score1.append(point[i])
#         but1.append(goal1[i])
#         score2.append(point[i])
#         but2.append(goal2[i])
#
#     print("\t \t \t \t Premier tour \n ")
#
#     for i in range(len(name)):
#         print("\t\t\t\t" + name[i] + " \t " + str(score1[i]) + " points " + str(but1[i]) + " buts")
#     print("=======================================================")
#
#     print("\t \t \t \t Second tour \n ")
#
#     for i in range(len(name)):
#         print("\t\t\t\t" + name[i] + " \t " + str(score2[i]) + " points " + str(but2[i]) + " buts")
#     print("=======================================================")
#
#     print("\t \t \t \t Classement Final \n ")
#
#     for i in range(len(name)):
#         print(
#             "\t\t\t\t" + name[i] + " \t " + str(score1[i] + score2[i]) + " points " + str(but1[i] + but2[i]) + " buts ")


# name = ["Henry", "Owen", "Drogba"]
# point = [0, 0, 0]
# goal1 = [18, 12, 6]
# goal2 = [6, 8, 5]
# gain = [6,4,2]
#
# name, goal1, goal2, point = trier(name, goal1, goal2, point)
# for i in range(len(name)):
#     point[i] += gain[i]
#
#
#
# name, goal2, goal1, point = trier(name, goal2, goal1, point)
# for i in range(len(name)):
#     point[i] += gain[i]
#
# print(name)
# print(point)
# print(goal1, goal2)

# def printOne(name, goal, title, current_pts):
#     print("\t\t\t\t{}\n".format(title))
#     for i in range(len(name)):
#         print("\t\t\t\t {} \t {} points {} buts".format(name[i], gain[i] ,goal[i]))
#     print("=======================================================")
#     return current_pts
#
# def trier(name, goal1, goal2, pts):
#     swap = True
#     while swap:
#         swap = False
#         for i in range(len(name) - 1):
#             if goal1[i + 1] < goal1[i]:
#                 name[i], name[i + 1] = name[i + 1], name[i]
#                 goal1[i], goal1[i + 1] = goal1[i + 1], goal1[i]
#                 goal2[i], goal2[i + 1] = goal2[i + 1], goal2[i]
#                 pts[i], pts[i + 1] = pts[i + 1], pts[i]
#                 swap = True
#     return name, goal1, goal2, pts
#
#
# name = ["Henry", "Owen", "Drogba"]
# point = [0,0,0]
# goal1 = [18, 12, 6]
# goal2 = [6, 8, 5]
# gain = [2,4,6]
#
# name, goal1, goal2, point = trier(name, goal1, goal2, point)
# point = printOne(name, goal1, "Premier tour", point)
#
# name, goal2, goal1, point = trier(name, goal2, goal1, point)
# point = printOne(name, goal2, "2nd tour", point)

#point = printTotal(name, goal1, "Total", point)

# import datetime
#
# now = datetime.datetime.now()
# s = now.hour * 3600 + now.minute * 60 + now.second
# print(s)

a = [0] * 5
b = a
c = a[:]

a[2] = 1
print(a ,"\n", b, "\n", c)
print(id(a), id(b), id(c))
