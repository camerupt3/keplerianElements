# Predicting the position and speed of the satellite at a given time (Lab 2)
# Coordinate System : Geocentric Equatorial
# Goal : to find coordinates and components of position vector, N hours after t0 (N - variant)

from main import *  # import all variables from main.py
import math
import numpy as np


# calculate eccentric anomaly (solve Kepler's equation by Fixed Point Iteration)

E0 = float(0)
epsilon = float(0.001)
N = 1   # variant
N_step = int(100)
t0 = 0
C1 = n*(t0 + N*3600)
print("e = ", e)
print("C1 = ",C1)


def f(E):
    return E - (e * np.sin(E)) - C1


def g(E):
    return (e * np.sin(E)) + C1


def fixedPointIteration(E0_func, epsilon_func, N_step_func):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        E1 = g(E0_func)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, E1, g(E1)))
        E0_func = E1

        step = step + 1

        if step > N_step_func:
            flag = 0
            break

        condition = abs(f(E1)) > epsilon_func

    if flag == 1:
        print('\nRequired root is: %0.8f' % E1)
    else:
        print('\nNot Convergent.')


# FPI input


fixedPointIteration(E0, epsilon, N_step)



