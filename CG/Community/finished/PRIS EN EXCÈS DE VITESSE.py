import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class voiture():
    def __init__(self, ID):
        self.plaque = ID
        self.dist = []
        self.time = []
        self.vitesse = []
        self.too_fast = []
        arr_car.append(self)
    
    def add_control(self,distance, temps):
        self.dist.append(distance)
        self.time.append(temps)
        
    def calc_vitesse(self, limit):
        for i in range(len(self.dist)-1):
            speed = 3600*(self.dist[i+1]-self.dist[i])/(self.time[i+1]-self.time[i])
            self.vitesse.append(speed)
            if speed > limit:
                self.too_fast.append(self.dist[i+1])

listing = []
arr_car = []
exces = []

l = int(input())
n = int(input())
for i in range(n):
    r = input()
    r = r.split(" ")
    if r[0] not in listing:
        listing.append(r[0])
        car = voiture(r[0])
    car.add_control(int(r[1]), int(r[2]))
    
for each_car in arr_car:
    each_car.calc_vitesse(l)
    if each_car.too_fast != []:
        exces.append([each_car.plaque, each_car.too_fast])
    
if len(exces) == 0:
    print("OK")
else:
    for each_car in exces:
        for each_exces in each_car[1]:
            print(each_car[0] + " " + str(each_exces))
    

# To debug: print("Debug messages...", file=sys.stderr)


