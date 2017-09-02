import math
from vpython import *

# s = sphere(pos = vector(0,0,0), radius = 0.5, color = color.green)
# s2 = sphere(pos = vector(3,0,0), radius = 0.5, color = color.red)
# l = paths.line(start=s, end=s2, np=2)
# L = paths.line(start=vector(1,0,0), end=vector(3,2,0), np=21)
# curve(pos=[(0,0,0), (1,0,0), (2,1,0)], radius=0.05)


from vpython.controls import *


c = controls()  # Crée une fenêtre pour les contrôles
# Crée un bouton dans la fenêtre des contrôles:
b = button(pos=(0, 0), width=60, height=60,
           text='Click me')
while 1:
    c.interact()