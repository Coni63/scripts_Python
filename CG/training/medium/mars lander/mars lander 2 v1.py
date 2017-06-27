import sys
import math

class robot():
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.power = 3
        self.angle = 0
        self.angle_real = 0
        self.fuel = 500
        
    def update(self, pos_x, pos_y, vit_x, vit_y, pet, angle, power):
        self.x = pos_x
        self.y = pos_y
        self.vx = vit_x
        self.vy = vit_y
        self.power = power
        self.angle = 0
        self.angle_real = angle
        self.fuel = pet

    def need_stab(self):
        if abs(self.vx) >= 20 or self.vy < -40:
            return True
        else:
            return False
    
    def reduire(self, vitesse):
        if self.vx>=0:
            self.angle = 10
        else:
            self.angle = -10
            
    def augmenter(self, vitesse):
        if self.vx>=0:
            self.angle = -10
        else:
            self.angle = 10
            
    def stabilize(self):
        if self.vy != 0:
            angle_inertiel = math.degrees(math.atan(self.vx/self.vy))
            
            if angle_inertiel < 20 and angle_inertiel >= 0:
                self.angle = -20
            elif angle_inertiel > -20 and angle_inertiel < 0:
                self.angle = 20
            else:
                self.angle = -int(angle_inertiel)
            
            if angle_inertiel*self.angle_real < 0:
                self.power = 4
            else:
                self.power = 0  
        else:
            self.power = 3
            self.angle = 0
        
    def has_good_traj(self):
        if self.vy != 0:
            delta_v = self.y - target[1]
            delta_h = -delta_v*self.vx/self.vy
            if abs(self.x+delta_h-target[0]) < 300:
                return True
            else:
                return False
        else :
            return True
        
    def correct(self):
        angle_inertiel = math.degrees(math.atan(self.vx/self.vy))
        angle_target = math.degrees(math.atan((target[0]-self.x)/(target[1]-self.y)))
        if abs(angle_inertiel) > abs(angle_target):
            self.reduire(self.vx)
            self.power = 4
        else:
            self.augmenter(self.vx)
            self.power = 4
        
        return True
        
    def is_landing(self):
        if self.y - target[1] < 150:
            return True
        else: 
            return False
        
    def land(self):
        self.angle = 0
        if self.vy > -30:
            self.power = 3
        elif self.vy <= -30:
            self.power = 4
        
    def show(self):
        print(self.angle, self.power)
    

surface_n = int(input())  # the number of points used to draw the surface of Mars.
surface = []

for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    surface.append([land_x, land_y])
    
for j in range(len(surface)-1):
    if surface[j][1] == surface[j+1][1] and surface[j+1][0]-surface[j][0] >= 1000:
        target = [int((surface[j][0]+surface[j+1][0])/2), surface[j][1]]
        
print(target, file=sys.stderr)

lander = robot()

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    lander.update(x, y, h_speed, v_speed, fuel, rotate, power)
    
    if lander.need_stab():
        print( lander.need_stab(), file=sys.stderr)
        lander.stabilize()
    #elif lander.has_good_traj() == False:
    #    lander.correct()
    #elif lander.is_landing():
    #    lander.land()
    lander.show()

    # To debug: print("Debug messages...", file=sys.stderr)

