import sys
import math
import time
from collections import defaultdict, deque

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
        
class Graphe:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)
  
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
        graph.add_node(depart)
        graph.add_node(arrive)
        distance = list_arret[depart].get_dist(list_arret[arrive])
        graph.add_edge(depart,arrive,distance)

try:

    if start_point == end_point:
        print(list_arret[start_point].name)
    else:
        result = shortest_path(graph, start_point, end_point)
        print('Distance mini = ', result[0], file=sys.stderr)
        for each in result[1]:
            print(list_arret[each].name)
except:
    print("IMPOSSIBLE")

interval = time.time() - start_time     
print("Total time in seconds : ", interval, file=sys.stderr)

# To debug: print("Debug messages...", file=sys.stderr)