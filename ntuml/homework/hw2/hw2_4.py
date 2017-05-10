# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 08:36:28 2017

@author: Yi
"""
import math
import matplotlib.pyplot as plt
    
def error_a(N, delta = 0.05, vc = 50):
    return math.sqrt(8.0/N*math.log(4*(2*N)**vc/delta))
    
def error_b(N, delta = 0.05, vc = 50):
    return math.sqrt(16.0/N*math.log(2*N**vc/math.sqrt(delta)))
    
def error_c(N, delta = 0.05, vc = 50):
    return math.sqrt(2.0*math.log(2*N*math.pow(N, vc))/N) + math.sqrt(2.0 / N * math.log(1.0 / delta)) + 1.0 / N
    
def error_d(N, delta = 0.05, vc = 50):
    return math.sqrt(math.log(6 * (2*N)**vc)/N + 1.0 / N**2) +  + 1.0 / N
    
def error_e(N, delta = 0.05, vc = 50):
    return math.sqrt(math.log(4 * (N**2)**vc)/(2*N-4.0) + 1.0 / (N-2)**2) +  + 1.0 / (N-2)
#4
all_N = range(3, 10000)
plt.plot(all_N, [error_a(N) for N in all_N], label='Original VC bound')
plt.plot(all_N, [error_b(N) for N in all_N], label='Rademacher Penalty Bound')
plt.plot(all_N, [error_c(N) for N in all_N], label='Parrondo and Van den Broek')
plt.plot(all_N, [error_d(N) for N in all_N], label='Devroye')
plt.plot(all_N, [error_e(N) for N in all_N], label='Variant VC bound')
plt.legend()
plt.show()

print('when N=10000, delta=0.02, vc=50')
print('error_a=', "%.2f" %error_a(10000))
print('error_b=', "%.2f" %error_b(10000))
print('error_c=', "%.2f" %error_c(10000))
print('error_d=', "%.2f" %error_d(10000))
print('error_e=', "%.2f" %error_e(10000))
#5
print('when N=5, delta=0.02, vc=50')
print('error_a=', "%.2f" %error_a(5))
print('error_b=', "%.2f" %error_b(5))
print('error_c=', "%.2f" %error_c(5))
print('error_d=', "%.2f" %error_d(5))
print('error_e=', "%.2f" %error_e(5))