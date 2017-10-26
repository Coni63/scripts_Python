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

# import datetime
#
# now = datetime.datetime.now()
# s = now.hour * 3600 + now.minute * 60 + now.second
# print(s)

# a = [0] * 5
# b = a
# c = a[:]
#
# a[2] = 1
# print(a ,"\n", b, "\n", c)
# print(id(a), id(b), id(c))

# from tkinter import *
#
# COLOR = "green"
#
# root = Tk()
#
# root.config(highlightbackground=COLOR)
# button = Button(text="button", borderwidth ="0")
# button.pack(padx=5, pady=5)
# button2 = Button(text="button", borderwidth ="2")
# button2.pack(padx=5, pady=5)
#
# root.mainloop()

# import matplotlib.pyplot as plt
# from pylab import *
#
# fig = plt.figure()
# matplotlib.rcParams['figure.figsize'] = [400, 50]
# fig.patch.set_facecolor('#2c3e50')
# #fig.patch.set_alpha(0.7)
#
# ax = fig.add_subplot(111)
#
# size = 75
# a, b, c = 1, 1.2, 0.75
# t = arange(0.0, 100, 100/size)
# s = a * (-1 + np.random.random(size))
# s2 = b * (-1 + np.random.random(size))
# s3 = c * (-1 + np.random.random(size))
#
# plot(t, s)
# plot(t, s2)
# plot(t, s3)
#
# ax.patch.set_facecolor('#2c3e50')
# #ax.patch.set_alpha(0.5)
#
# ax.axes.get_xaxis().set_visible(False)
# ax.axes.get_yaxis().set_visible(False)
# ax.axis('off')
# plt.tight_layout()
#
# # If we don't specify the edgecolor and facecolor for the figure when
# # saving with savefig, it will override the value we set earlier!
# fig.savefig('header-bg.png', facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0, dpi=199)
# plt.show()

# import uuid
#
# class Abc:
#     def __init__(self, id2 = uuid.uuid4()):
#         self.ID = id2
#
#     def __repr__(self):
#         return "{}".format(self.ID)
#
# for _ in range(10):
#     a = Abc()
#     print(a)

# print(list('abc'))
#
# print(list(map(str, 'abc')))
#
# L = [
#     {"value": 1, "other_value": 4},
#     {"value": 2, "other_value": 3},
#     {"value": None, "other_value": 2},
#     {"value": 4, "other_value": 1},
#     {"value": None, "other_value": 42},
#     {"value": 3, "other_value": 9001}
# ]
#
# def weighted(nb):
#     if nb is None:
#         return -float('inf')
#     else:
#         return nb
#
# L.sort(key=lambda x:weighted(x["value"]), reverse=True)
# print(L)
#
#
# import timeit
#
#
# def f1():
#     a = {}
#     for i in range(1000):
#         a[i] = i
#     return a
#
# def f2():
#     a = {}
#     for i in range(1000):
#         a[str(i)] = i
#     return a
#
# def f3():
#     a = {}
#     for i in range(1000):
#         a[(i, i)] = i
#     return a
#
# def f4():
#     a = {}
#     for i in range(1000):
#         a[(str(i), str(i))] = i
#     return a
#
# def f5():
#     for i in range(1000):
#         str(i)
#
# print(timeit.timeit("f1()", number = 1000, setup="from __main__ import f1"))
# t1 = timeit.timeit("f2()", number = 1000, setup="from __main__ import f2")
# print(timeit.timeit("f3()", number = 1000, setup="from __main__ import f3"))
# t2 = timeit.timeit("f4()", number = 1000, setup="from __main__ import f4")
# tstr = timeit.timeit("f5()", number = 1000, setup="from __main__ import f5")
# print(t1-tstr)
# print(t2-2*tstr)
#

# class Eleve:
#     def __init__(self, nom, notes = []):
#         self.nom = nom
#         self.notes = notes
#         self.pts = 0
#         self.score = 0
#         self.set_fitness()
#
#     def __repr__(self):
#         return "{}(diff : {}) a {} pts \n".format(self.nom, self.score ,self.pts)
#
#     def set_fitness(self):
#         self.score = self.notes[1] - self.notes[0]
#
#
# nom = ["Fred", "Alain", "Marc", "Emile"]
# note1 = [12, 10, 8, 9]
# note2 = [16, 10, 4, 23]
# note_global = list(zip(note1, note2))
# print(note_global) # pack des note par eleve
#
# # creation des instance d'eleves
# liste_eleve = []
# for i in range(4):
#     liste_eleve.append(Eleve(nom[i], note_global[i]))
#
# # tous les eleve sont stocke dans ce tableau
# print(liste_eleve)
#
# # on les trie par notes
# liste_eleve.sort(key=lambda x:x.score, reverse=True)
# print(liste_eleve)
#
# # on attribut les pts
# score = [6,4,2,0]
# for i, each in enumerate(liste_eleve):
#     each.pts = score[i]
# print(liste_eleve)

# import distutils
# print(distutils.spawn.find_executable('ffmpeg'))

# from math import pi
# liste = [0.1, 1, 10, 100, 88.8]
# for diam in liste:
#     #diam = float(diam)
#     r = diam/2
#     section = 2 * pi * r**2
#     aire = 4 * pi * r**2
#     vol = 4/3 * pi * r**3
#     phrase = "Diamètre: {:8.2f} cm - Section: {:8.2f} cm² - Aire: {:8.2f} cm² - Volume: {:8.2f} cm³\n"
#     print(phrase.format(diam, section, aire, vol))

# import math
# max_angle = math.radians(20)
# print(max_angle)

# def batch(elem, batch_size):
#     size = len(elem)
#     for i in range(size//batch_size):
#         yield elem[:batch_size]
#         elem = elem[batch_size:]
#
# a = list(range(50))
# gen = batch(a, 5)
#
# print(next(gen))
# print(next(gen))
# print(next(gen))

# import numpy as np
#
# a = np.random.rand(50) > 0.5
# print(a)
#
# c = np.random.randint(0,5, 50)
# print(c)
#
# b = np.argwhere(a==True)
# print(b)
#
# print(c[b])
#
# import sys
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
#
# def window():
#     win = QWidget()
#     win.setGeometry(100, 100, 800, 300)  # La taille est arbitraire
#
#     # ==== Début des erreurs de type NameError ====
#     # Création de deux boutons (1) et (2) reliés aux fonctions f1 et f2
#     # Bouton n°1
#     b1 = QPushButton("foo", win)
#     b1.clicked.connect(f1)
#
#     # Bouton n°2
#     b2 = QPushButton("bar", win)
#     b2.clicked.connect(f2)
#
#     # Création d'un menu horizontal composé des deux boutons
#     # menu = QHBoxLayout()
#     # menu.addWidget(b1)
#     # menu.addWidget(b2)
#
#     # Affichage des widgets de l'application
#     # win.setLayout(menu)  # Ajout de la barre de menu dans fenetre
#     # ==== Fin des erreurs de type NameError ====
#     win.setTitle("Application test")
#     win.show()
#     sys.exit(app.exec_())
#
#
# def f1():
#     print("Bouton n°1 a été cliqué !")
#
#
# def f2():
#     print("Bouton n°2 a été cliqué !")
#
#
# if __name__ == "__main__":
#     app = QGuiApplication(sys.argv)
#     window()

# import itertools
#
# list1=['cat','animal']
# list2=['dog','animal']
# list3=['crow','bird']
#
# l = list(zip(list1, list2, list3))
#
#
# for k, l in itertools.groupby(l), key= lambda x:x[1]):
#     print(k, l)

# import numpy as np
# s = np.random.normal(22.5, 0.1, 144)
# arr = [[x] for x in s]
# print(arr)

# import numpy as np
# from sklearn.svm import LinearSVC
#
# X = [[1,1], [2,0], [2,3]]
# y = [0, 0, 1]
#
# svc = LinearSVC(C=1, loss="hinge")
# svc.fit(X, y)
#
#
# print(svc.coef_ , svc.intercept_ )

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import pylab
# import os
# import time
#
# def generator():
#     while True:
#         yield np.random.random(2)
#
# plt.axis() #[0, 1, 0, 1]
# plt.ion()
#
# # for i in range(100):
# #     x, y = np.random.random(2)
# #     plt.scatter(i, y)
# #     plt.pause(0.05)
# gen = generator()
#
# while True:
#     x, y = next(gen)
#     plt.scatter(x, y)
#     plt.pause(0.5)
# plt.show()
#
# pylab.waitforbuttonpress(timeout=-1)
#
# # while True:
# #     plt.pause(0.05)

# import datetime
# import time
#
# def to_date(str_date):
#     return datetime.datetime.strptime(str_date, "%d/%m/%Y")
#
# list1=["04/05/2004","07/02/2002","12/05/1993"]
#
# #conversion
# list1 = list(map(to_date, list1))
# # ou
# list1 = [to_date(x) for x in list1]
#
# #trie
# list1.sort()
#
# # affichage en format anglais
# for date in list1:
#     print(datetime.datetime.strftime(date, "%m-%d-%Y"))

# # import numpy as np
# n=2
# # mat = np.zeros(dtype=np.bool, shape=(n,n))
# # print(mat)
# # for line in range(n):
# #     for col in range(n):
# #         mat[line, col] = (1 == int(input("t")))
# # print(mat)
#
# mat = [[False for _ in range(n)] for _ in range(n)]
# print(mat)

# import numpy as np
#
# X = np.array([-0.78768,-1.51760513,0.74416271,-0.62288928])
# Y = np.array([-34.59703199, -30.79543532, 19.31018182, -19.44809959])
# b = [52,13,29,32]
#
#
# for a in b:
#     z = Y - a*X
#     print(np.matmul(np.transpose(z), z))

# import os
# import pickle
#
# def create_file():
#     emplacement = input("A quel emplacement voudrez-vous enregistrer le fichier (le nom du fichier est genere automatiquement) ?\n")
#     emplacement_bf = os.path.join(emplacement, "generateur_de_nom.txt")
#     open(emplacement_bf, 'a').close()   # creer un fichier vide (c'est l'objectif de la fonction)
#     with open('save.pickle', 'wb') as f:
#         pickle.dump(emplacement_bf, f)
#     return emplacement_bf               # pour avoir ensuite l'url directement
#
# def charger(save_file = None):
#     if save_file is None:               # si tu ne founi pas d'url il va chercher un pickle
#         try:
#             save_file = pickle.load(open("save.pickle", "rb"))
#         except:
#             print("Pas de sauvegarde")
#             return False
#
#     with open(save_file, 'r') as f:
#         for line in f:
#             print(line)
#
# def generate(save_file = None):
#     if save_file is None:
#         save_file = create_file()                   # si tu ne fournis pas de fichier il en crée un
#
#     with open(save_file, 'w') as f:
#         f.write("Hello World")                      # ecrire ce que tu veux dedans
#
# if __name__ == "__main__":
#     #create_file()           # creer le fichier vide a l'url voulu et sauvegarde l'url dans pickle
#     #generate()              # me demande l'url pour creer le fichier
#     #generate("F:/Nicolas/PycharmProjects/Python_Scripts/generateur_de_nom.txt")   # Ajoute Hello world au fichier
#     #charger()                                                                      # Affiche Hello World s'il trouve le pickle
#     #charger("F:/Nicolas/PycharmProjects/Python_Scripts/generateur_de_nom.txt")     # Affiche Hello World
#
#


# liste = ['orange','cerveau','elephant','tri','chat','orangoutan','dinosaures']
# print(list(filter(lambda x: len(x)>8 ,liste))) => ['orangoutan', 'dinosaures']

# import random
#
# liste = ['orange', 'cerveau', 'elephant', 'tri', 'chat', 'orangoutan', 'dinosaures']
# liste = [mot for mot in liste if len(mot) > 8]
# choix = random.sample(liste, 1)
#
# a = 0
# while (a <= 8):
#     essaie = input("Veuillez deviner une lettre qui fait partie du mot")
#     for i, elt in enumerate(choix[0]):
#         if elt == essaie:
#             print(elt)
#         else:
#             print("*")
#     a = a + 1

# class Foo:
#     def __init__(self, nom, val):
#         self.nom = nom
#         self.score = val.get("score", 0)
#         self.partie = val.get("parties", 0)
#
#     def __repr__(self):
#         return "{} a joue {} parties et a {} pts".format(self.nom, self.score, self.partie)
#
# tableau = {
# 'Ludovic': {'score': 1, 'parties': 1},
# 'Bertrand': {'score': 45, 'parties': 14},
# 'Joseph': {'score': 47, 'parties': 45},
# }
#
# instances = []
#
# for key, value in tableau.items():
#     obj = Foo(key, value)
#     print(obj)
#     instances.append(obj)
#
# print(instances)

# import matplotlib.pyplot as plt
# import math
#
# m = 0.055
# k = 0.0187
# g = 9.81
#
# def Trajectoiref(x_min, x_max, nb_step, X0, Y0, V0, alpha):
#     alpha = math.radians(alpha)
#     step = (x_max - x_min) / nb_step
#     T = 0 #[x_min + step*i for i in range(nb_step)]        # equivaut a un linspace (ca ne te sert pas dans ton code donc pas besoin de le calculer ensuite
#     X = X0
#     Y = Y0
#     V_x = V0 * math.cos(alpha)
#     V_y = V0 * math.sin(alpha)
#     for _ in range(nb_step*2):
#         X += V_x * step
#         Y += V_y * step
#         V_x -= step*((k / m)*V_x**2)
#         V_y -= step*((k / m)*V_y**2)
#         V_y -= 9.81*step/1000
#         #print(T, X, Y, V_x, V_y)
#         #V = math.sqrt(V_x**2 + V_y**2)
#         plt.scatter(X, Y)
#     plt.show()
#     #return (T, X, Y, V_x, V_y)
#
#
# T, X, Y, Xp, Yp = Trajectoiref(0, 1, 100, 0, 0, 3, 18)
# # plt.plot(X, Y)  # afficher les courbes
# # plt.show()

# a = "1101"
# s=0
# for power, digit in enumerate(a[::-1]):
#     s+=int(digit)*(2**power)
#
# print(s)

# import multiprocessing
# import numpy as np
# import time
#
# L = list(range(1000000))
# np.random.shuffle(L)
#
#
# def f(x=None):
#     (L[:].sort())
#     return 0
#
#
# t1 = time.clock()
# with multiprocessing.Pool(processes=3) as pool:
#     pool.map(f, range(5))
# print(time.clock() - t1)
#
# t1 = time.clock()
# results = [f() for _ in range(5)]
# print(time.clock() - t1)

# import numpy as np
#
# def factolu(A):
#     n=np.shape(A)[0]
#     L = np.identity(n)
#     U = np.zeros(shape=(n,n))
#     for i in range(0, n-1):
#         for j in range(i+1, n):
#             L[j,i] = A[j,i]/A[i,i]
#             for k in range(i + 1, n):
#                 A[j:k] -= L[j, i] * U[i, k]
#         for j in range(i, n):
#             U[i,j] = A[i,j]
#     U[-1,-1] = A[-1,-1]
#     return L, U
#
# t = np.random.random(size=(3,3))
# print(t, "\n")
# l, u = factolu(t)
# print(l, "\n\n", u, "\n")
#
# print(np.matmul(l, u))
#
# import functools
# ton_booleen = functools.reduce(lambda a, b: a * b, list(map(ord, ["c", "a"])))%2==0
# print(ton_booleen)


import seaborn as sns
import pylab as plt


def onpick(event):
    print(event)
    print(event.__dict__)


iris = sns.load_dataset("iris")
species = iris.pop("species")
clusterobj = sns.clustermap(iris)

clusterobj.ax_heatmap.set_xticklabels([])
clusterobj.ax_heatmap.set_yticklabels([])

clusterobj.fig.canvas.mpl_connect('figure_leave_event', onpick)

print(clusterobj.ax_row_dendrogram)
print(clusterobj.dendrogram_row.dendrogram)

plt.show()
