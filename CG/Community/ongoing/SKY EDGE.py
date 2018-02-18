import sys
import math
import time
import copy

class Crew:
    def __init__(self):
        self.crew = []
        
    def add(self, m):
        self.crew.append(m)
    
    def get_older(self):
        for member in self.crew:
            member.age += 1
    
    def make_baby(self, mini, maxi):
        batch = 0
        for member in self.crew:
            if mini <= member.age <= maxi:
                batch += member.nb
            
        if batch // 10 > 0:
            self.add(Member(0, batch // 10))
            
    def remove_dead(self, maxi):
        for i in range(len(self.crew)):
            if self.crew[i].age > maxi:
                self.crew.pop(i)
                break
    
    def crew_size(self):
        crew_size = 0
        for member in self.crew:
            crew_size += member.nb
        return crew_size
        
    def show(self):
        for member in self.crew:
            print(member.age, member.nb, file = sys.stderr)
        print("", file = sys.stderr)
        
        
class Member:
    def __init__(self, age, nb):
        self.age = age
        self.nb = nb

def simulate(LIFE_EXPECTANCY, team):
    LIMIT_BIRTH = int(LIFE_EXPECTANCY/2)
    for travel_time in range(1, y+1):
        team.get_older()
        team.make_baby(20, LIMIT_BIRTH)
        team.remove_dead(LIFE_EXPECTANCY)
        size =  team.crew_size()
        if size > c:
            return "Above"
        if size == 0:
            return "Below"
        #print("%s year, crew = %s" % (travel_time, size), file = sys.stderr)
        #team.show()
        #print("", file = sys.stderr)
    if 200 <= size <= c:
        return "Ok"
    else:
        return "Below"
        

y = int(input())
c = int(input())
n = int(input())

the_crew = Crew()
for i in range(n):
    age, number = [int(j) for j in input().split()]
    the_crew.add(Member(age, number))
    
MIN_LIFE_EXPECTANCY = 1
MAX_LIFE_EXPECTANCY = 1500

start_time = time.time()

for i in range(20):
    val = int((MAX_LIFE_EXPECTANCY + MIN_LIFE_EXPECTANCY)/2)
    result = simulate(val, copy.deepcopy(the_crew))
    if result == "Above":
        MAX_LIFE_EXPECTANCY = val
    elif result == "Below":
        MIN_LIFE_EXPECTANCY = val
    else:
        while True:
            MAX_LIFE_EXPECTANCY += 1
            result = simulate(MAX_LIFE_EXPECTANCY, copy.deepcopy(the_crew))
            if result == "Above":
                break
            elif result == "Below" or result == "Ok":
                MAX_LIFE_EXPECTANCY += 1
            print(MAX_LIFE_EXPECTANCY,file=sys.stderr)
        while True:
            MIN_LIFE_EXPECTANCY += 1
            result = simulate(MIN_LIFE_EXPECTANCY, copy.deepcopy(the_crew))
            if result == "Below":
                break
            elif result == "Above" or result == "Ok":
                MIN_LIFE_EXPECTANCY -= 1
        break
    
    t = "%s ms" % (1000*(time.time()-start_time))
    print(MIN_LIFE_EXPECTANCY, MAX_LIFE_EXPECTANCY, t,  file=sys.stderr)

print(MIN_LIFE_EXPECTANCY, MAX_LIFE_EXPECTANCY)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)