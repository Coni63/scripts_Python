import sys
import math
from collections import defaultdict

def get_order(pos, distance):
    arr = []
    while len(arr)<=i:
        min_val = 1000
        node = -1
        for each in distance[pos].keys():
            if distance[pos][each] <= min_val and distance[pos][each] > 0 and each not in arr:
                min_val=distance[pos][each]
                node = each
        arr.append(node)
        pos = node
    return arr
        
def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return len(path)-1
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

class Graphe(object):
	def __init__(self):
		self.graphe = {}

	def ajouteSommet(self, sommet):
		if sommet not in self.graphe.keys():
			self.graphe[sommet] = []

	def ajouteArrete(self, sommet, sommetVoisin):
		if sommet != sommetVoisin:
			self.graphe[sommetVoisin].append(sommet)
			self.graphe[sommet].append(sommetVoisin)

	def supprimeSommet(self, sommet):
		for sommetVoisin in self.graphe[sommet]:
			self.graphe[sommetVoisin].remove(sommet)
		del self.graphe[sommet]

	def supprimeArrete(self, sommet, sommetVoisin):
		self.graphe[sommetVoisin].remove(sommet)
		self.graphe[sommet].remove(sommetVoisin)
		print(sommet, sommetVoisin)

graph = Graphe()
list_gate = []
list_node = []
critical_node = {}
dist = {}
order_gate = []

node, link, gate = [int(i) for i in input().split()]

for i in range(node):
    graph.ajouteSommet(i)
    list_node.append(i)

for i in range(link):
    n1, n2 = [int(j) for j in input().split()]
    graph.ajouteArrete(n1, n2)

for i in range(gate):
    ei = int(input())  # the index of a gateway node
    list_gate.append(ei)
    
print(list_gate, file=sys.stderr)  

for each in list_node:
    hub_in_touch = list(set(graph.graphe[each]) & set(list_gate)) #on recup les hub en contact
    if len(hub_in_touch) >= 2: #si le noeud est lié a 2+ gate
        critical_node[each] = hub_in_touch

for each_start in list_node:
    for each_gate in list_gate:
        longueur = bfs(graph.graphe, each_start, each_gate)
        if each_start in dist.keys():
            dist[each_start][each_gate]=longueur
        else:
            dist[each_start]={}
            dist[each_start][each_gate]=longueur

#print(graph.graphe, file=sys.stderr)
#print(list_gate, file=sys.stderr)
#print(critical_node, file=sys.stderr)
#print(dist, file=sys.stderr)
#print("****************", file=sys.stderr)

while True:
    skynet = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    
    intersection = list(set(graph.graphe[skynet]) & set(list_gate))
    
    if len(intersection) == 1:
        graph.supprimeArrete(intersection[0], skynet)
    
    elif len(critical_node.keys())>0:
        order_gate = get_order(skynet, dist) #return the order of node tried by skynet
        #print(order_gate, file=sys.stderr)
        flag = False
        a = ""
        b = ""
        for every_gate in order_gate: #pour chaque gate que va essayer skynet
            for each_critical_node in critical_node.keys(): #si il y a un noead critique
                if every_gate in critical_node[each_critical_node]  and flag == False :
                    a = each_critical_node
                    b = critical_node[a][0]
                    graph.supprimeArrete(a, b)
                    flag = True
        
        if flag: #si on a fermé un noead on le supprime des double gate
            del critical_node[a]  
            
    else: #si on a aucun des 2 precedent on ferme un noead au pif, de toute facon c'est win
        for each in order_gate:
            if len(graph.graphe[each])>0:
                a = each
                b = graph.graphe[each][0]
                graph.supprimeArrete(a, b)