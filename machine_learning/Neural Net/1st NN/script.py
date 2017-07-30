# -*-coding:Latin-1 -*
import numpy as np
import random


def sigmoide(x, deriv=False):
    if deriv:
        return ((x) * (1 - (x)))
    return (1 / (1 + np.exp(-x)))


X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0],
              [1],
              [1],
              [0]])

syn0 = 2 * np.random.random((2, 4)) - 1
syn1 = 2 * np.random.random((4, 4)) - 1
syn2 = 2 * np.random.random((4, 1)) - 1

epsi = 10
nbIte = 5000

for j in range(0, nbIte):
    l1 = sigmoide(np.dot(X, syn0))
    l2 = sigmoide(np.dot(l1, syn1))
    l3 = sigmoide(np.dot(l2, syn2))

    l3_delta = (y - l3) * sigmoide(l3, deriv=True)
    l2_delta = l3_delta.dot(syn2.T) * sigmoide(l2, deriv=True)
    l1_delta = l2_delta.dot(syn1.T) * sigmoide(l1, deriv=True)

    syn2 += l2.T.dot(l3_delta) * epsi
    syn1 += l1.T.dot(l2_delta) * epsi
    syn0 += X.T.dot(l1_delta) * epsi

print("e")
print((y - l3))
print("sortie")
print(l3)