import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def traj_f(syst, t):
    [x, y, vx, vy] = syst
    alpha = math.atan(vy/vx)
    dxdt = vx
    dydt = vy
    dvxdt = -(k / m) * (vx ** 2) * math.cos(alpha)
    dvydt = -(k / m) * (vy ** 2) * math.sin(alpha) - g
    return (dxdt, dydt, dvxdt, dvydt)

def traj(syst, t):
    [x, y, vx, vy] = syst
    alpha = math.atan(vy/vx)
    dxdt = vx
    dydt = vy
    dvxdt = 0
    dvydt = - g
    return (dxdt, dydt, dvxdt, dvydt)

r = 0.01 # 1cm en m
cx = 10# 0.3
rho = 1.225 # 1.225kg/m3
s = math.pi*(r**2)
steel_density = 7800 # 7800kg/m^3 pour l'acier
m = 4/3 * math.pi * math.pow(r, 3) * steel_density # Vol * density
k = cx*rho*s/2
g = 9.81

t = np.linspace(0, 2.5, 100)
systCI = [0,1,10,10]     #x,y,vx,vy

sols = odeint(traj, systCI, t)
sols = sols[sols[:,1]>0]
x = sols[:,0]
y = sols[:,1]
plt.plot(x, y)

sols = odeint(traj_f, systCI, t)
sols = sols[sols[:,1]>0]
x = sols[:,0]
y = sols[:,1]
plt.plot(x, y)

plt.show()
