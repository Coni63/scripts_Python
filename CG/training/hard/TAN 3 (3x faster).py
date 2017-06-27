import sys
import math
import time
from collections import defaultdict, deque
import heapq 

def shortest_path(G, start, end):
   def flatten(L):       # Flatten linked list of form [0,[1,[2,[]]]]
      while len(L) > 0:
         yield L[0]
         L = L[1]

   q = [(0, start, ())]  # Heap of (cost, path_head, path_rest).
   visited = set()       # Visited vertices.
   while True:
      (cost, v1, path) = heapq.heappop(q)
      if v1 not in visited:
         visited.add(v1)
         if v1 == end:
            return list(flatten(path))[::-1] + [v1]
         path = (v1, path)
         for (v2, cost2) in G[v1].items():
            if v2 not in visited:
               heapq.heappush(q, (cost + cost2, v2, path))

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
        list_arret[self.ID]=self #on retourne dans un dictionnaire l'objet lie a son ID
    
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
    route = route.split()
    depart = route[0][len(prefix_Station):]
    arrive = route[1][len(prefix_Station):]
    if depart != arrive:
        graph.ajouteSommet(depart)
        graph.ajouteSommet(arrive)
        distance = list_arret[depart].get_dist(list_arret[arrive])
        graph.ajouteArrete(depart, arrive, distance)

try:
    if start_point == end_point:
        print(list_arret[start_point].name)
    else:
        result = shortest_path(graph.graphe, start_point, end_point)
        #print('Distance mini = ', result, file=sys.stderr)
        for each in result:
            print(list_arret[each].name)
except:
    print("IMPOSSIBLE")

interval = time.time() - start_time     
print("Total time in seconds : ", interval, file=sys.stderr)

# To debug: print("Debug messages...", file=sys.stderr)