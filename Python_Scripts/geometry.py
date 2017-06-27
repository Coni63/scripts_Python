from sympy import *
from sympy.geometry import *
from sympy.plotting import plot

import math

x = Point(0, 0)
y = Point(1, 1)
z = Point(2, 2)
zp = Point(1, 0)
print(Point.is_collinear(x, y, z))

print(Point.is_collinear(x, y, zp))

t = Triangle(zp, y, x)
print(t.area)
print(t.medians[x])

Segment(Point(1, S(1)/2), Point(0, 0))

m = t.medians
intersection(m[x], m[y], m[zp])
c = Circle(x, 5)
l = Line(Point(5, -5), Point(5, 5))
c.is_tangent(l) # is l tangent to c?
l = Line(x, y)
c.is_tangent(l) # is l tangent to c?
intersection(c, l)

R_pref = 11
R_opening = 10

Center_gate = Point(0, 0)
Gate = Circle(Center_gate, R_pref)

Top_flat_width = 0.4
alpha = math.acos(1-(Top_flat_width/R_pref))
print(alpha)
Top_flat_height = -R_pref*sin(alpha)
print(Top_flat_height)
Top_flat_left = Point(R_pref-Top_flat_width, Top_flat_height)
Top_flat_right = Point(R_pref, Top_flat_height)

l = Line(Top_flat_left, Top_flat_right)
print(l)

plot_implicit(l.equation(), range=(-15, 15))
