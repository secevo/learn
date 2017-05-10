# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:51:12 2017

@author: Yi
"""

import sympy

x = sympy.symbols('x')
f = 4*((2*x)**10)*sympy.exp(-0.125*(0.05**2)*x) - 0.05
print(sympy.solve(f , x))