import sys
import math
from copy import deepcopy

def debug(args)
    print( .join(map(str, args)) , file=sys.stderr)

class Point()
    def __init__(self, X=0, Y=0)
        self.x = X
        self.y = Y
        
    def offset(self, dx, dy)
        self.x += dx
        self.y += dy
        
    def show(self)
        print( {} , {} .format(self.x, self.y) , file=sys.stderr)
    
class Segment()
    def __init__(self, p1, p2)
        self.p1 = p1
        self.p2 = p2
    
    def length(self)
        return ((self.p2.x - self.p1.x)2 + (self.p1.y-self.p2.y)2)0.5
        
    def slope(self)
        if self.p2.x != self.p1.x
            return (self.p1.y-self.p2.y)  (self.p1.x-self.p2.x)
        else
            return float('inf')
    
    def origin(self)
        if math.isinf(self.slope())
            return None
        else
            return p1.y - self.slope p1.x
    
    def to_vector(self)
        self.vector = Vector_2D()
        self.vector.create(self.p2, self.p1)
        return self.vector
        
    def mid(self)
        m = Point((self.p1.x + self.p2.x)2 , (self.p1.y + self.p2.y)2)
        return m
        
    def show(self)
        print( ({}, {}) to ({}, {}) .format(self.p1.x, self.p1.y, self.p2.x, self.p2.y) , file=sys.stderr)
     
class Vector_2D()
    def __init__(self, X=0, Y=0)
        self.x = X
        self.y = Y
        
    def norm(self)
        return (self.x2 + self.y2)0.5
    
    def normalize(self)
        self.x = self.norme
        self.y = self.norme
    
    def det(self, other_vector)
        return self.xother_vector.y - self.yother_vector.x
    
    def scalar(self, other_vector)
        if self.norm() != 0 and other_vector.norm() != 0
            return ((self.xother_vector.x)+(self.yother_vector.y)) 
        else
            return None
        
    def angle(self, other_vector)
        if not self.scalar(other_vector) is None
            alpha = math.acos(self.scalar(other_vector)  (self.norm()other_vector.norm()))
            alpha = math.degrees(alpha)
            alpha = math.copysign(alpha, self.det(other_vector))
            return alpha
        else
            return None
            
    def rotate(self, angle)
        angle = math.radians(angle)
        X = self.x  math.cos(angle) - self.y  math.sin(angle)
        Y = self.x  math.sin(angle) + self.y  math.cos(angle)
        self.x = X
        self.y = Y
        
    def show(self)
        print( {} , {} .format(self.x, self.y) , file=sys.stderr)
        
    def create(self, p1, p2)
        self.x = p2.x - p1.x
        self.y = p2.y - p1.y
        

class Relief()
    def __init__(self, size)
        self.size = size
        self.surface = []
        self.segment = []
        self.target = Point()
        
    def add_point(self, X, Y)
        self.surface.append(Point(X, Y))
        
    def set_landing_position(self)
        for j in range(self.size-1)
            seg = Segment(self.surface[j], self.surface[j+1])
            self.segment.append(seg)
            if seg.slope() == 0 and seg.length() = 1000
                self.target = seg.mid()
                self.target.offset(0,1500)

class Robot()
    def __init__(self)
        self.position = Point()
        self.speed = Vector_2D(0, 0)
        self.acceleration = Vector_2D(0, 0)
        self.power = 3
        self.angle = 0
        self.fuel = 500
        self.phase = 1
        
    def update(self, pos_x, pos_y, vit_x, vit_y, pet, angle, power)
        self.position.x = pos_x
        self.position.y = pos_y
        self.speed.x = vit_x
        self.speed.y = vit_y
        self.acceleration.x = -powermath.sin(math.radians(angle))
        self.acceleration.y = powermath.cos(math.radians(angle))-3.711
        self.power = power
        self.angle = angle
        self.fuel = pet
                
    def show(self)
        attrs = vars(self)
        print( ''.join(%s %sn % item for item in attrs.items()), file = sys.stderr)
        
    def print_result(self)    
        print(int(self.angle), int(self.power))
    

surface_n = int(input())  # the number of points used to draw the surface of Mars.

Mars = Relief(surface_n)

for i in range(surface_n)
    land_x, land_y = [int(j) for j in input().split()]
    Mars.add_point(land_x, land_y)
    
Mars.set_landing_position()

Lander = Robot()

#test = Vector_2D(-1,-1)
#p1 = Point(10, 10)
#p2 = Point(15, 5)
#s1 = Segment(p1, p2)
#s1.to_vector()

MAX_ANGLE = 20
MAX_H_SPEED = 20
MAX_V_SPEED = 40

loop = 0

while True
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    Lander.update(x, y, h_speed, v_speed, fuel, rotate, power)
    debug(x, y, h_speed, v_speed)
    
    if Lander.phase == 1
        if loop % 10 == 0
            anchor_position = deepcopy(Lander.position)
            trajectoire = Segment(Mars.target, anchor_position)
            vect_trajectoire = trajectoire.to_vector()
        angle_vit_traj = vect_trajectoire.angle(Lander.speed)
        if not angle_vit_traj is None
            angle_prop = 90-angle_vit_traj
            Lander.angle = min(angle_prop, math.copysign(MAX_ANGLE, angle_prop))
        else
            Lander.angle = 0
        Lander.power = 4
        trajectoire.show()
        
    #debug(Lander.speed.angle(test))
    
    loop += 1
    Lander.print_result()
    
    
    print(0, 1)
    
    # To debug print(Debug messages..., file=sys.stderr)

