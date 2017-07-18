import sys
import math

def andrew(S):
    S.sort()
    top = []
    bot = []
    for p in S:
        while len(top) >=2 and not left_turn(p, top[-1], top[-2]):
            top.pop()
        top.append(p)
        while len(bot) >=2 and not left_turn(bot[-2], bot[-1], p):
            bot.pop()
        bot.append(p)
    return bot[:-1] + top[:0:-1]
        

def left_turn(a, b, c):
    return (a[0]-c[0])*(b[1]-c[1]) - (a[1]-c[1])*(b[0]-c[0]) > 0
    
class Segment:
    def __init__(self, p1, p2):
        self.P1 = p1
        self.P2 = p2
        self.V = (p2[0] - p1[0], p2[1] - p1[1])
        self.is_vertical = (p2[0] == p1[0])
        self.is_horizontal = (p2[1] == p1[1])
        self.origine = None
        self.pente = None
        self.abscisse = None
        self.set_equation()
        
    def __repr__(self):
        if self.is_vertical:
            return "X = {}".format(self.abscisse)
        elif self.is_horizontal:
            return "Y = {}".format(self.origine)
        else:
            return "Y = {}x+{}".format(self.pente, self.origine)
            
    def set_equation(self):
        if self.is_vertical:
            self.abscisse = self.P2[0]
        elif self.is_horizontal:
            self.origine = self.P2[1]
            self.pente = 0
        else:
            self.pente = self.V[1]/self.V[0]
            self.origine = self.P1[1] - self.pente * self.P1[0]
            
    def intersect(self, autre_segment):
        if self.is_vertical and autre_segment.is_vertical:
            return [False, -1, -1]
        elif self.is_horizontal and autre_segment.is_horizontal:
            return [False, -1, -1]
        else:
            if self.is_vertical:
                y_intersect = autre_segment.pente * self.abscisse + autre_segment.origine
                if min(autre_segment.P1[1], autre_segment.P2[1]) < y_intersect < max(autre_segment.P1[1], autre_segment.P2[1]):
                    return [True, self.abscisse, y_intersect]
                else:
                    return [False, -1, -1]
            elif autre_segment.is_vertical:
                y_intersect = self.pente * autre_segment.abscisse + self.origine
                if min(autre_segment.P1[1], autre_segment.P2[1]) < y_intersect < max(autre_segment.P1[1], autre_segment.P2[1]):
                    return [True, autre_segment.abscisse, y_intersect]
                else:
                    return [False, -1, -1]
            else:
                if self.pente == autre_segment.pente:
                    return [False, -1, -1]
                else:
                    x_intersect = (autre_segment.origine - self.origine)/(self.pente-autre_segment.pente)
                    y_intersect = self.pente * x_intersect + self.origine
                    if min(autre_segment.P1[0], autre_segment.P2[0]) < x_intersect < max(autre_segment.P1[0], autre_segment.P2[0]):
                        return [True, x_intersect, y_intersect]
                    else:
                        return [False, -1, -1]
            
def squared_dist(x1, y1, x2, y2):
    return math.pow((x2-x1), 2) + math.pow((y2-y1), 2)


def set_corner(resultat, x1, y1, x2, y2):
    global corner
    k = 10000
    V_mouvement = (x2-x1, y2-y1)
    V_normal = (-V_mouvement[1], V_mouvement[0])
    intersection = ((x1+x2)/2, (y1+y2)/2)
    point_1 = (intersection[0] - k*V_normal[0], intersection[1] - k*V_normal[1])
    point_2 = (intersection[0] + k*V_normal[0], intersection[1] + k*V_normal[1])
    bissectrice = Segment(point_1, point_2)
    #print(bissectrice, file=sys.stderr)
    
    corner_buffer = []
    for i in range(len(corner) + 1):
        P1 = corner[i % len(corner)]
        P2 = corner[(i+1) % len(corner)]
        #print(P1, P2, file=sys.stderr)
        cote = Segment(P1, P2)
        #print(cote, file=sys.stderr)
        intersection = bissectrice.intersect(cote) # retourner [intersection_bool, X, Y]
        #print(intersection, file=sys.stderr)
        if intersection[0] == True:
            corner_buffer.append(( intersection[1], intersection[2] ))
    corner += corner_buffer
        
    for i in reversed(range(len(corner))):
        pts = corner[i]
        is_montant = (y2-y1 > 0)
        go_to_right = (x2 > x1)
        is_flat = (y2 == y1)
        if not is_flat:
            if (resultat == "WARMER" and is_montant) or (resultat == "COLDER" and not is_montant):
                if bissectrice.pente * pts[0] + bissectrice.origine <= pts[1]: # si le points est au dessus du segment
                    pass
                else:
                    del corner[i]
            elif (resultat == "WARMER" and not is_montant) or (resultat == "COLDER" and is_montant):
                if bissectrice.pente * pts[0] + bissectrice.origine >= pts[1]: # si le points est au dessus du segment
                    pass
                else:
                    del corner[i]
        else:
            if (resultat == "WARMER" and go_to_right) or (resultat == "COLDER" and not go_to_right): # on garde la partie droite
                if pts[0] >= bissectrice.abscisse: 
                    pass
                else:
                    del corner[i]
            elif (resultat == "WARMER" and not go_to_right) or (resultat == "COLDER" and go_to_right): # on garde la partie gauche
                if pts[0] <= bissectrice.abscisse : # si le points est au dessus du segment
                    pass
                else:
                    del corner[i]
    
    corner = andrew(corner)

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

current_position = (x0, y0)
previous_position = (0, 0)
visited = []

while True:
    bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
    
    if bomb_dir != "UNKNOWN":
        set_corner(bomb_dir, *previous_position, *current_position)
    else:
        if w == 1:
            corner = [(0, 0), (0, h-1)] 
        elif h == 1:
            corner = [(0, 0), (w-1, 0)]
        else:
            corner = [(0, 0), (w-1, 0), (w-1, h-1), (0, h-1)]
    
    #print(corner, file=sys.stderr)
        
    dist_max = 0
    for each in corner:
        current_distance = squared_dist(*each, *current_position)
        if current_distance > dist_max:
            target = each
            dist_max = current_distance
    previous_position, current_position = current_position, target
    #print("from {} to {}".format(previous_position, current_position), file=sys.stderr)
    t = list(map(round, target))
    if t in visited:
        del corner[corner.index(t)]
        t = ( min(t[0]+1, w-1), min(t[1]+1, h-1) )
        corner.append(t)
    visited.append(t)
    print("{:d} {:d}".format(*t))
    