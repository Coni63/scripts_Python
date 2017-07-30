# -*-coding:Latin-1 -*
import numpy as np
import random

def sigmoide(x, deriv=False):
    if deriv:
        return ((x) * (1 - (x)))
    return (1 / (1 + np.exp(-x)))


X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
Y = np.array([[0],
              [1],
              [1],
              [0]])


class NeuralNet:
    """ Crée un réseau de neurones, nbNeurons est une liste qui indique pour chaque couche le nombre de neurones associés.
    La première étant l'entrée et la dernière la sortie. """

    def __init__(self, nbNeurons):
        self.nbNeurons = nbNeurons
        self.syn = []
        self.l = [0 for i in range(len(self.nbNeurons))]
        self.l_delta = self.l[:]
        for i in range(0, len(nbNeurons) - 1):
            self.syn.append(2 * np.random.random((nbNeurons[i], nbNeurons[i + 1])) - 1)

    def train(self, X, Y, nbIte=None, epsi=10):
        """ nbIte : nombre d'itérations ; epsi : learning rate. """
        self.l[0] = X
        loop = 0
        if nbIte is not None:
            for j in range(0, nbIte):

                """ On calcule les sorties des layers : """
                for i in range(1, len(self.nbNeurons)):
                    self.l[i] = sigmoide(np.dot(self.l[i - 1], self.syn[i - 1]))

                """ On calcule les delta des layers : """
                self.l_delta[len(self.nbNeurons) - 1] = (Y - self.l[len(self.nbNeurons) - 1]) * sigmoide(
                    self.l[len(self.nbNeurons) - 1], deriv=True)
                for i in range(len(self.nbNeurons) - 2, 0, -1):
                    self.l_delta[i] = self.l_delta[i + 1].dot(self.syn[i].T) * sigmoide(self.l[i], deriv=True)

                """ On ajuste les poids : """
                for i in range(len(self.nbNeurons) - 2, -1, -1):
                    self.syn[i] += self.l[i].T.dot(self.l_delta[i + 1]) * epsi

        else:
            d = 1
            while d > 0.015 and loop < 20000:
                """ On calcule les sorties des layers : """
                for i in range(1, len(self.nbNeurons)):
                    self.l[i] = sigmoide(np.dot(self.l[i - 1], self.syn[i - 1]))

                """ On calcule les delta des layers : """
                self.l_delta[len(self.nbNeurons) - 1] = (Y - self.l[len(self.nbNeurons) - 1]) * sigmoide(
                    self.l[len(self.nbNeurons) - 1], deriv=True)
                for i in range(len(self.nbNeurons) - 2, 0, -1):
                    self.l_delta[i] = self.l_delta[i + 1].dot(self.syn[i].T) * sigmoide(self.l[i], deriv=True)

                """ On ajuste les poids : """
                for i in range(len(self.nbNeurons) - 2, -1, -1):
                    self.syn[i] += self.l[i].T.dot(self.l_delta[i + 1]) * epsi

                error = Y - self.l[-1]
                d = sum(abs(x) for x in error)
                loop += 1

        print(self.nbNeurons, loop)
        # print("e")
        # print((Y - self.l[-1]))
        # print("sortie")
        # print(self.l[-1])
        return loop


shape = [
    [2,4,1],
    [2,5,1],
    [2,6,1],
    [2,4,4,1],
    [2,5,5,1],
    [2,6,6,1]
]

for setup in shape:
    arr = []
    for i in range(10):
        n = NeuralNet(setup)
        arr.append(n.train(X=X, Y=Y, nbIte=None, epsi=10))
    print(sum(arr)/10)