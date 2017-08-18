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


import timeit


def f1():
    a = {}
    for i in range(1000):
        a[i] = i
    return a

def f2():
    a = {}
    for i in range(1000):
        a[str(i)] = i
    return a

def f3():
    a = {}
    for i in range(1000):
        a[(i, i)] = i
    return a

def f4():
    a = {}
    for i in range(1000):
        a[(str(i), str(i))] = i
    return a

def f5():
    for i in range(1000):
        str(i)

print(timeit.timeit("f1()", number = 1000, setup="from __main__ import f1"))
t1 = timeit.timeit("f2()", number = 1000, setup="from __main__ import f2")
print(timeit.timeit("f3()", number = 1000, setup="from __main__ import f3"))
t2 = timeit.timeit("f4()", number = 1000, setup="from __main__ import f4")
tstr = timeit.timeit("f5()", number = 1000, setup="from __main__ import f5")
print(t1-tstr)
print(t2-2*tstr)


