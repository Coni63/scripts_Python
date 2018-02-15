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

class Reaper:
    def __init__(self, ID, T, X, Y, VX, VY, S):
        self.ID = ID
        self.team = T
        self.x = X
        self.y = Y
        self.vx = VX
        self.vy = VY
        self.stored_water = S
        
    def get_pos(self):
        r = math.sqrt(self.x*self.x+self.y*self.y)
        alpha = math.asin(self.y/(r+1))
        return r, alpha
        
class Wreck:
    def __init__(self):
        self.ID = ID
        self.radius = R
        self.x = X
        self.y = Y

# game loop

ref = None
while True:
    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    
    radius_list = []
    wreck_list = []
    unit_count = int(input())
    for i in range(unit_count):
        unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2 = input().split()
        unit_id = int(unit_id)
        unit_type = int(unit_type)
        player = int(player)
        mass = float(mass)
        radius = int(radius)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        extra = int(extra)
        extra_2 = int(extra_2)
        
        if unit_type == 4:
            wreck_list.append((x, y))
            radius_list.append(math.sqrt(x*x+y*y))
            
        if player == 0:
            my_car = Reaper(unit_id, player, x, y, vx, vy, extra)
            
    wreck_list = andrew(wreck_list)
    
    avg_rad = sum(radius_list)//len(radius_list)
    
    closest = 1e6
    for i, wreck in enumerate(wreck_list):
        d = math.sqrt((my_car.x-wreck[0])**2+(my_car.y-wreck[1])**2)
        if d < closest:
            closest = d
            ref = i  
    target = wreck_list[ref]
    print("{} {} {}".format(target[0], target[1], 300))
    
    ### V2
    # if ref == None:
    #     closest = 1e6
    #     for i, wreck in enumerate(wreck_list):
    #         d = math.sqrt((my_car.x-wreck[0])**2+(my_car.y-wreck[1])**2)
    #         if d < closest:
    #             closest = d
    #             ref = i  
    # else:
    #     target = wreck_list[ref]
    #     d = math.sqrt((my_car.x-wreck[0])**2+(my_car.y-wreck[1])**2)
    #     if d < 400:
    #         ref = (ref+1)%len(wreck_list)   
    # target = wreck_list[ref]
    # print("{} {} {}".format(target[0], target[1], 300))
    
    ### V2
    # current_rad, current_angle = my_car.get_pos()
    # print(current_rad, current_angle, file=sys.stderr)
    # if abs(current_rad-avg_rad) < 800:
    #     next_x = int(avg_rad * math.cos(current_angle+10*3.14/180))
    #     next_y = int(avg_rad * math.sin(current_angle+10*3.14/180))
    #     print("{} {} {}".format(next_x, next_y, 300))
    # else:
    #     if current_rad > avg_rad:
    #         print("aaa", file=sys.stderr)
    #         print("0 0 300")
    #     else:
    #         print("afdg", file=sys.stderr)
    #         print("{} 0 300".format(int(avg_rad)))
            
    print("WAIT")
    print("WAIT")
    print("WAIT")