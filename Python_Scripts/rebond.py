import math

class Point:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def avancer(self, vit, step = 1):
        self.x += vit.x * step
        self.y += vit.y * step

    def __repr__(self):
        return "{},{}".format(self.x, self.y)


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.vecteur_directeur = None
        self.vecteur_normal = None

    def vect_dir(self):
        x = self.p2.x - self.p1.x
        y = self.p2.y - self.p1.y
        self.vecteur_directeur = Vecteur(x, y)
        return self.vecteur_directeur

    def vect_norm(self):
        if self.vecteur_directeur is None:
            self.vect_dir()
        self.vecteur_normal = Vecteur(-self.vecteur_directeur.y, self.vecteur_directeur.x)
        return self.vecteur_normal


class Vecteur:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y
        self.norme = 0
        self.set_norme()

    def set_norme(self):
        self.norme = math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        self.set_norme()
        self.x /= self.norme
        self.y /= self.norme

    def scalar(self, other_vect):
        return self.x * other_vect.x + self.y * other_vect.y

    def mult(self, a):
        self.x = self.x * a
        self.y = self.y * a

    def plus(self, v):
        self.x += v.x
        self.y += v.y

    def minus(self, v ):
        self.x -= v.x
        self.y -= v.y

    def __repr__(self):
        return "{},{}".format(self.x, self.y)

def rebond(normale, vitesse):
    norme_vitesse_proj = vitesse.scalar(normale)
    print(norme_vitesse_proj)
    print(normale)
    normale.mult(2*norme_vitesse_proj)
    print(normale)
    vitesse.minus(normale)
    print(vitesse)

x1 = Point(0, 10)
x2 = Point(10, 10)
l1 = Line(x1, x2)

radius = 1
balle = Point(2, 8)
vitesse = Vecteur(1, 3)

AC = l1.vect_norm()
AC.normalize()

print(AC)

vitesse = rebond(AC, vitesse)

# for i in range(100):
#     l2 = Line(x1, balle)
#     AB = l2.vect_dir()
#     distance_balle_line = abs(AB.scalar(AC))
#     if distance_balle_line < radius:
#         vitesse = rebond(AC, vitesse)
#     else:
#         balle.avancer(vitesse, step = 0.01)
#         #print(balle)