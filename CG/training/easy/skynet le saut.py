import sys
import math

def get_Max_Speed(init_speed, road_length):
    inc_speed_up=0
    distance = inc_speed_up*init_speed + inc_speed_up*(inc_speed_up+1)/2
    
    while road_length - distance > init_speed:
        distance = inc_speed_up*init_speed + inc_speed_up*(inc_speed_up+1)/2
        inc_speed_up+=1
       
    slow = road_length - distance
        
    return [inc_speed_up, slow]
        
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

inc = 0
max = [0,0]
jump = False

# game loop
while True:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.
    
    if speed > gap+1:
        print("SLOW")
    
    if speed <= gap and jump == False:
        print("SPEED")
    
    if speed == gap+1 and road-coord_x>=speed and jump == False:
        print("WAIT")
    
    if road-coord_x<=speed and jump == False:
        print("JUMP")
        jump= True
        
    if jump == True:
        print("SLOW")
        
    #    inc += 1
    
    #if inc==0:
    #    max = get_Max_Speed(speed,road)
    #    inc+=1 
    
    #if jump==True:
    #    print("SLOW")  
    #if speed == 0:
    #    print("SPEED")
    #if speed == 1 and coord_x < max[1]:
    #    print("WAIT")
    #if coord_x >= slow and jump==False and inc < max[0]:
    #    print("SPEED")
    #    inc += 1
    #if inc == max[0]:
    #    print("JUMP")
    #    jump = True
    

        
        
    
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    
