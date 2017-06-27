import sys
import math
import this



def fight(W, L, tie = None):
    if tie == None:
        F = 1
    else:
        F = 0.5
    W.ratio()
    L.ratio()
    D = W.score - L.score
    P = 1 / (1 + 10 ** (-D / 400))
    W.score += W.K * (F-P)
    L.score += W.K * ((1-F)-(1-P))
    W.nb_match += 1
    L.nb_match += 1

class Player:
    def __init__(self, N, P):
        self.name = N
        self.score = int(P)
        self.nb_match = 0
        self.K = 40
        Player_list[self.name] = self

    def ratio(self):
        if self.nb_match < 30:
            self.K = 40
        else:
            if self.score <= 2400:
                self.K = 20
            else:
                self.K = 10
        print(self.name, self.nb_match, self.K)

A = "toto:1900"
B = "titi:2000"
C = "toto win titi"

A1, A2 = A.split(":")
B1, B2 = B.split(":")

Player_list = {}

p1 = Player(A1, A2)
p2 = Player(B1, B2)

for _ in range(50):
    fight(p1, p2)
    print(p1.score, p2.score)

#2191.6523811306993 1708.3476188692991