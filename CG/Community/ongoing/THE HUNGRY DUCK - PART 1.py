import sys
import math
from collections import defaultdict

def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths


class Node:
    instances = {}
    start = None
    def __init__(self, x, y, S):
        self.x = x
        self.y = y
        self.val = S
        self.name = str(x)+"-"+ str(y)
        Node.instances[self.name] = self
        if self.x == 0 and self.y == 0 : 
            Node.start = self
        
    def __repr__(self):
        return "({},{})".format(self.x, self.y)

class Tree:
    def __init__(self):
        self.graph = {}
        
    def create_node(self):
        for each_node in Node.instances.values():
            self.graph[each_node] = []
            right_cell_name = str(each_node.x+1)+"-"+str(each_node.y)
            bottom_cell_name = str(each_node.x)+"-"+str(each_node.y+1)
            right_cell = Node.instances.get(right_cell_name)
            bottom_cell = Node.instances.get(bottom_cell_name)
            if not right_cell is None:
                self.graph[each_node].append(right_cell)
            if not bottom_cell is None:
                self.graph[each_node].append(bottom_cell)

G = Tree()
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input().split()
    for j in range(w):
        val = int(line[j])
        Node(j, i , val)

#for each in Node.instances.values():
#    print(each, file=sys.stderr)
    
G.create_node()
#print(G.graph, file=sys.stderr)


all_paths  = DFS(G.graph, Node.start)

max_food = max( sum(n.val for n in p) for p in all_paths)

print(max_food)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


