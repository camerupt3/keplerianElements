# KEPLERIAN ELEMENTS FINDER (LAB 1)
# by Aisy Maffaz

import numpy as np
import warnings

# all values are in SI units

# take in required elements from user

x = int(input("Enter x value (in km):"))
print("ok")
y = int(input("Enter y value (in km):"))
print("ok")
z = int(input("Enter z value (in km):"))
print("ok")

Vx = int(input("Enter Vx value (in km/s):"))
print("ok")
Vy = int(input("Enter Vy value (in km/s):"))
print("ok")
Vz = int(input("Enter Vz value (in km/s):"))
print("ok")

"""
x = -3200
y = 8200
z = 5800
Vx = 5
Vy = -2
Vz = 6
"""


# define standard grav. parameter of earth

mew = 398600    # unit in km3/s2


# find area vector

r = np.array([x, y, z])
v = np.array([Vx, Vy, Vz])
c = np.cross(r, v)
print("c = ", c)


# convert vector to magnitude


def mag(vector):
    return np.linalg.norm(vector)


warnings.filterwarnings('ignore')   # ignore RuntimeWarning
cMag = mag(c)

# print("cMag= ", cMag)


# calculate p

p = (pow(cMag, 2))/mew
print("P = ", p)


# find Laplace vector and its mag

f = (np.cross(v, c)) - ((mew/mag(r))*r)
fMag = mag(f)


# find eccentricity

e = fMag/mew
print("e = ", e)


# find z-component of c

cz = (c[2])
cz_new = abs(cz)


# find inclination of orbit (angle between z-axis and area vector(c))
# if cz is -ve, take 180 - i

if cz < 0:
    i = 180 - np.degrees(np.arccos(cz_new/cMag))
    print("i = ", i)

else:
    i = np.degrees(np.arccos(cz/cMag))
    print("i = ", i)


# define unit vectors

ex = np.array([1, 0, 0])
ez = np.array([0, 0, 1])


# find unit vector in direction of AN

c = np.array(c, dtype='int64')  # to correct for integer overflow
cx = c[0]
# print("cx = ", cx)
cy = c[1]
# print("cy = ", cy)
c_vec = np.array([-cy, cx, 0])
lhs = 1/(np.sqrt(pow(cx, 2) + pow(cy, 2)))
eN = lhs * c_vec
# print("eN = ", eN)


# check if need to subtract LAN by 2pi and find LAN

eTest = np.dot((np.cross(ex, eN)), ez)

if eTest > 0:
    LAN = np.rad2deg(np.arccos(-(cy*lhs)))

else:
    LAN = np.rad2deg((2*np.pi) - (np.arccos(-(cy * lhs))))

print("LAN = ", LAN)


# argument of periapsis
AOP_test = np.dot((np.cross(eN, f)), c)
AOP_calc = (np.arccos((np.dot(eN, f))/fMag))

if AOP_test > 0:
    AOP = np.rad2deg(AOP_calc)
else:
    AOP = np.rad2deg((2*np.pi) - AOP_calc)


print("AOP = ", AOP)


# true anomaly (angle after pericenter)

rMag = mag(r)
ta = (np.arccos((np.dot(f, r)) / (fMag * rMag)))

if np.dot(np.cross(f, r), c) > 0:
    TA = ta

else:
    TA = (2*np.pi) - ta


# time after periapsis

u = AOP + TA    # latitude argument
vMag = mag(v)
h = pow(vMag, 2) - ((2*mew)/rMag)
a = -(mew/h)
E_init = 2*np.arctan((np.sqrt((1-e)/(1+e))) * np.tan(TA/2))
n = np.sqrt(mew/pow(a, 3))  # average motion
tpi = (E_init - (e * np.sin(E_init)))/n
print("tpi = ", tpi)    # in seconds
