import sys
import math
import time
from collections import namedtuple
from collections import defaultdict

def plus_court(etape):
    """
    Trouve récursivement la plus courte chaine entre debut et fin avec l'algo de Dijkstra
    visites est une liste et dist et pere des dictionnaires 
    graphe  : le graphe étudié                                                               (dictionnaire)
    étape   : le sommet en cours d'étude                                                     (sommet)
    end_point     : but du trajet                                                            (sommet)
    visites : liste des sommets déjà visités                                                 (liste de sommets)
    dist    : dictionnaire meilleure distance actuelle entre départ et les sommets du graphe (dict sommet : int)
    pere    : dictionnaire des pères actuels des sommets correspondant aux meilleurs chemins (dict sommet : sommet)
    start_point   : sommet global de départ                                                  (sommet)
    Retourne le couple (longueur mini (int), trajet correspondant (liste sommets)) 
       
    """
    # si on arrive à la fin, on affiche la distance et les peres
    if etape == end_point:
        trajet = []
        extremite = end_point
        while extremite != start_point:   
            trajet = [extremite] + trajet
            extremite = pere[extremite]
        return dist[end_point], [start_point] + trajet
        #return dist[fin], affiche_peres(pere,depart,fin,[])
    
    # si c'est la première visite, c'est que l'étape actuelle est le départ : on met dist[etape] à 0
    if len(visites) == 0 : dist[etape]=0
    
    # on commence à tester les voisins non visités
    for voisin in graph.graphe[etape]:
        if voisin not in visites:
            # la distance est soit la distance calculée précédemment soit l'infini
            dist_voisin = dist.get(voisin, float('inf'))
            # on calcule la nouvelle distance calculée en passant par l'étape
            candidat_dist = dist[etape] + graph.graphe[etape][voisin]
            # on effectue les changements si cela donne un chemin plus court
            if candidat_dist < dist_voisin:
                dist[voisin] = candidat_dist
                pere[voisin] = etape
    
    # on a regardé tous les voisins : le noeud entier est visité
    visites.append(etape) 
    non_visites.remove(etape)
    
    maxi = float('inf')
    for each in non_visites:
        if dist.get(each, float('inf')) < maxi:
            maxi = dist[each]
            noeud_plus_proche = each
    
    return plus_court(noeud_plus_proche)
     


class arret():
    def __init__(self, stop):
        stop = stop.split(",")
        self.ID = stop[0][len(prefix_Station):]
        self.name = stop[1][1:-1]
        self.description = stop[2]
        self.latitude = math.radians(float(stop[3]))
        self.longitude = math.radians(float(stop[4]))
        self.zone = stop[5]
        self.url = stop[6]
        self.type_arret = stop[7]
        self.station_parent = stop[8]
        list_arret[self.ID]=self
    
    def get_dist(self, node2):
        x = (node2.longitude-self.longitude)*math.cos((self.longitude+node2.longitude)/2)
        y = node2.latitude-self.latitude
        d = 6371*math.sqrt(x**2+y**2)
        return d

class Graphe(object):
	def __init__(self):
		self.graphe = {}

	def ajouteSommet(self, sommet):
		if sommet not in self.graphe.keys():
			self.graphe[sommet] = {}

	def ajouteArrete(self, sommet, sommetVoisin, p):
		self.graphe[sommet][sommetVoisin]=p

start_time = time.time()  
graph = Graphe()
list_arret = {}
visites = []
dist = {}
pere = {}
prefix_Station = 'StopArea:'

start_point = input()[len(prefix_Station):]
end_point = input()[len(prefix_Station):]

n = int(input())
for i in range(n):
    stop_name = input()
    arret(stop_name)  

m = int(input())
for i in range(m):
    route = input()
    route = route.split(" ")
    depart = route[0][len(prefix_Station):]
    arrive = route[1][len(prefix_Station):]
    if depart != arrive:
        graph.ajouteSommet(depart)
        graph.ajouteSommet(arrive)
        distance = list_arret[depart].get_dist(list_arret[arrive])
        graph.ajouteArrete(depart, arrive, distance)

non_visites=list(graph.graphe.keys())

try:
    if start_point == end_point:
        print(list_arret[start_point].name)
    else:
        l, c = plus_court(start_point)
        print('Distance mini = ', l, file=sys.stderr)
        for each in c:
            print(list_arret[each].name)
except:
    print("IMPOSSIBLE")
    
interval = time.time() - start_time     
print("Total time in seconds : ", interval, file=sys.stderr)

# To debug: print("Debug messages...", file=sys.stderr)