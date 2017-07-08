class data:
    instances = {}
    def __init__(self):
        self.PWs = 0
        self.K = []
        self.data1 = []
        self.data2 = []
        self.instances[self.PWs] = self

    def __repr__(self):
        print("PKs = {} \n K = {} \n Data1 = {} \n Data2 = {}".format(self.PWs, self.K, self.data1, self.data2))

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_liste(s):
    return s.count("-") == 2


with open("data.txt") as f:
    for i, line in enumerate(f):
        if i % 3 == 0:
            d = data()
            pws = [float(x) for x in line.split() if is_float(x)][0]
            liste = [[float(x) for x in Y.split("-")] for Y in line.split() if is_liste(Y)]
            d.PWs = pws
            d.K = liste[0]
        elif i % 3 == 1:
            d.data1 = [float(x) for x in line.split()]
        elif i % 3 == 2:
            d.data2 = [float(x) for x in line.split()]

for key, item in data.instances.items():
    print(item)