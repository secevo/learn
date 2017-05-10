# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:27:02 2017

@author: Fidel
"""

from sympy import exp,diff,symbols, Matrix

u, v = symbols('u v')
E = exp(u)+exp(2*v)+exp(u*v)+u**2-2*u*v+2*v**2-3*u-2*v
du = diff(E,u)
dv = diff(E,v)
duu = diff(du, u)
duv = diff(du, v)
dvv = diff(dv, v)
H = Matrix([[duu, duv], [duv, dvv]])
G = Matrix([du, dv])
delta = H.inv()*G

#6
print('#6', G, G.subs([(u,0),(v, 0)]))

#7
(x, y) = (0, 0)
for i in range(5):
    x = x - 0.01 * du.subs([(u,x),(v, y)])
    y = y - 0.01 * dv.subs([(u,x),(v, y)])
print('#7', E.subs([(u,x),(v, y)]))

#8
print('#8', H, H.subs([(u,0),(v, 0)]))

#10
(x, y) = (0, 0)
for i in range(5):
    x = x - 1.0 * delta[0].subs([(u,x),(v, y)])
    y = y - 1.0 * delta[1].subs([(u,x),(v, y)])
print('#9', E.subs([(u,x),(v, y)]))