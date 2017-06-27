import math
import numpy as np
import matplotlib.pyplot as plt
 
import scipy.integrate as sc
  
mt = 5.972e24 # masse terre en kg
ml = 7.3477e22 # masse lune en kg

rt = 6371e3 # rayon terre en m
rl = 1737e3 # rayon terre en m

dist_t_l = 384400 # dist terre lune en km

G = 6.67408e-11 #const gravitationnel

omegaterre = 2*math.pi / (24 * 60 * 60) # considere une periode de rotation de 24h et non 23 h 56 min et 4,3
omegalune  =  2*math.pi / (29.5 * 24 * 60 * 60) #considere Période synodique de la lune

rl  = 363104000
rzero = 6400000+35784

sigma = mt/ml # ratio masse terre / masse lune
mu = rl/rzero 

tc = np.sqrt(rzero**3/(G*ml))

def f(U,t):
    r0 = U[0]
    r1 = U[1]
    t0 = U[2]
    t1 = U[3]
    LS = np.sqrt(mu**2 + 1 - 2 * np.cos(t0)*mu*r0)
    r2 = - (sigma/r0**2) - (r0/LS**3) + r0*t1**2
    t2 =  - (mu*np.sin(t0)/(r0*LS**3)) - (2*r1*t1/r0)
    return(np.array([r1,r2,t1,t2]))
 
 
def adimensionnement( r0,r1,t0,t1,t):
    r0 = 1
    r1 = r1*tc/rzero
    t0 = t0
    t1 = t1 * tc
    t = t/tc
    return (np.array([r0,r1,t0,t1,t]))   
         
# CONDITIONS INITIALES (cf rzero pour r0):
r0 = rzero
r1 = 0
t0 = 0
t1 = omegaterre - omegalune
t = 72000

arr = [r0,r1,t0,t1]
#arr = adimensionnement(r0,r1,t0,t1,t)
U0 = arr

T = np.linspace(0,t,250)
sols = sc.odeint(f, U0, T)
print(sols)

"""
plt.subplot(4,1,1)
plt.plot (T,U[:,0],label="rl0")
plt.legend()
plt.subplot(4,1,2)
plt.plot (T,U[:,1])
plt.subplot(4,1,3)
plt.plot (T,U[:,2])
plt.subplot(4,1,4)
plt.plot (T,U[:,3])
plt.show()
"""