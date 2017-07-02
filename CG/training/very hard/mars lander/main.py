import math
import matplotlib.pyplot as plt

def combinaison_lineaire(A,B,u,v):
    return [A[0]*u+B[0]*v,A[1]*u+B[1]*v]

def interpolation_lineaire(A,B,t):
    return combinaison_lineaire(A,B,t,1-t)

def point_bezier_3(points_control,t):
    x=(1-t)**2
    y=t*t
    A = combinaison_lineaire(points_control[0],points_control[1],(1-t)*x,3*t*x)
    B = combinaison_lineaire(points_control[2],points_control[3],3*y*(1-t),y*t)
    return [A[0]+B[0],A[1]+B[1]]

def courbe_bezier_3(points_control,N):
    if len(points_control) != 4:
        raise SystemExit("4 points de controle")
    dt = 1.0/N
    t = dt
    points_courbe = [points_control[0]]
    while t < 1.0:
        points_courbe.append(point_bezier_3(points_control,t))
        t += dt
    points_courbe.append(points_control[3])
    return points_courbe

f = plt.figure(figsize=(7, 3))
position = [6500, 2000]
target = [0, 0]
sol = [ [0, 1800],
        [300, 1200],
        [1000, 1550],
        [2000, 1200],
        [2500, 1650],
        [3700, 220],
        [4700, 220],
        [4750, 1000],
        [4700, 1650],
        [4000, 1700],
        [3700, 1600],
        [3750, 1900],
        [4000, 2100],
        [4900, 2050],
        [5100, 1000],
        [5500, 500],
        [6200, 800],
        [6999, 600],
     ]

for i in range(len(sol)-1):
    a, b = sol[i], sol[i+1]
    plt.plot([a[0], b[0]], [a[1], b[1]], color="red")
    if a[1] == b[1] and abs(a[0] - b[0]) >= 1000:
        target = [(a[0] + b[0]) / 2, b[1]]

for i, val in enumerate(sol):
    plt.scatter(val[0], val[1], color="red")
plt.scatter(position[0], position[1], color="blue")
plt.scatter(target[0], target[1], color="green")

target_offset = [target[0], target [1]+300]
vitesse = 6000
angle = 25
vitesse = [position[0] - vitesse*math.cos(math.radians(angle)), position[1] + vitesse*math.sin(math.radians(angle))]
test = [ position, vitesse, target_offset, target ]

points = courbe_bezier_3(test, 50)
points_T = list(zip(*points))
plt.plot(points_T[0], points_T[1])

plt.grid()
plt.show()