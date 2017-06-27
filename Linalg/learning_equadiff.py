import math
import numpy as np
import matplotlib.pyplot as plt
 
import scipy.integrate as sc

# from http://www.prepas.org/2013/Info/Luminy/Gonnord-Lundi/equations-differentielles-python.pdf

#################################
########### Exemple 1 ###########
#################################

# def f(syst, t):
#     x, y = syst
#     eq1 = - y - x * (x**2 + y**2)
#     eq2 = x - y * (x**2 + y**2)
#     return [eq1, eq2]

# def f2(syst, t):
#     x, y = syst
#     eq1 = - y - x / 10 * (x**2 + y**2)
#     eq2 = x + y / 10 * (x**2 + y**2)
#     return [eq1, eq2]

# def f3(syst, t):
#     x, y = syst
#     eq1 = - y + x / 20 * (x**2 + y**2)
#     eq2 = x + y / 20 * (x**2 + y**2)
#     return [eq1, eq2]


# T = np.linspace(0, 20, 250)
# CI = [0, 1]
# sols = sc.odeint(f, CI, T)
# sols2 = sc.odeint(f2, CI, T)
# sols3 = sc.odeint(f3, CI, T)

# x = sols[:,0]
# y = sols[:,1]

# x2 = sols2[:,0]
# y2 = sols2[:,0]

# x3 = sols3[:,0]
# y3 = sols3[:,0]
# , x3, y3, 'g^'
# plt.plot(x, y, 'r--', x2, y2, 'bs')
# plt.show()

#################################
########### Exemple 2 ###########
#################################

# def f4(syst, t):
#     v, y = syst
#     dydt = v
#     dvdt = -dydt + 6*y
#     return [dvdt, dydt]

# T = np.linspace(0, 10, 100)
# CI = [-6, 2]
# sols = sc.odeint(f4, CI, T)

# x = sols[:,0]
# y = sols[:,1]

# plt.plot(y, T)
# plt.show()

#################################
########### Exemple 3 ###########
#################################

# def f5(syst, t):
#     x, z, dxdt, dzdt = syst
#     dxdt2 = dxdt #x
#     dzdt2 = dzdt #z
#     dx2dt = 0
#     dz2dt = -g
#     return [dxdt2, dzdt2, dx2dt, dz2dt]

# g = 9.81
# v0 = 10
# alpha = [ math.radians(10*x) for x in range(1, 9) ]
# T = np.linspace(0, 2, 100)

# for angle in alpha :
#     CI = [0, 0, v0*math.cos(angle), v0*math.sin(angle)]
#     sols = sc.odeint(f5, CI, T)

#     sols = sols[sols[:,1]>0,:] # remove all lines where col2 is < 0

#     x = sols[:,0]
#     z = sols[:,1]

#     plt.plot(x, z)
# plt.show()



# =========>>>>>>>> System 2DDL <<<<<<<<============

#################################
########### Exemple 4 ###########
#################################

# def f6(syst, t):
#     y, dydt = syst
#     dy2dt = -(b/a)*dydt + -(c/a)*y
#     return [dydt, dy2dt]

# a = 1
# b = 2
# c = 2

# T = np.linspace(0, 10, 100)
# CI = [1, 2]
# sols = sc.odeint(f6, CI, T)

# y = sols[:,0]

# plt.plot(T, y)
# plt.show()


#################################
########### circuit RL ##########
#################################

def tangente(a, b, x):
    return a*x+b

def f6(Is, t):
    didt = (U-R*Is)/L
    return didt

U = 5 
R = 2
L = 2

Tau = L/R
Uf = U/R

T = np.linspace(0, 7*Tau, 250)
I0 = 0
sols = sc.odeint(f6, I0, T)

plt.plot(T, sols)
plt.plot(Tau, 0.63*Uf, 'r^', 3*Tau, 0.95*Uf, 'g^')


tan_fact = (sols[1]-sols[0])/(T[1]-T[0])
tan_h = 0

tan = tangente(tan_fact, tan_h, T)
#print(tan[ tan<Uf :])
#tan = tan[ tan<Uf :]
plt.axis(ymax = 1.2*Uf)
plt.axvline(x=Tau)
plt.axhline(y=Uf)
plt.plot(T, tan)
plt.show()