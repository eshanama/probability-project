# Jennibelle Khuu (kuf3yd) and Esha Nama (esn4wx)

# import math libraries
import math
import numpy as np

# Section 1: Random Number Generator ---------------------------------------------------------------------

# starting value (seed)
x_0 = 1000
# multiplier
a = 24693
# increment
c = 3517
# modulus
K = 2**17

# linear congruential random number generator
def xi_random_num(i):
    if i == 0:
        return ((a)*(x_0)+c) % K
    else:
        return ((a)*xi_random_num(i-1)+c) % K

def random_num(n):
    num = xi_random_num(n)
    return num / K

# checking first three random numbers
print("u_0: " + str(random_num(0)))             # should be 0.4195
print("u_1: " + str(random_num(1)))             # should be 0.0425
print("u_2: " + str(random_num(2)) + "\n")      # should be 0.1274

print("u_51: " + str(random_num(51)))
print("u_52: " + str(random_num(52)))
print("u_53: " + str(random_num(53)) + "\n")

# Section 2: Random Variable Generator -------------------------------------------------------------------
# 2a: Discrete Random Variable

def xi_discrete_rv(t):
    return 1 - pow(math.e, (-1/12)*t)

def discrete_rv_generator(u):
    Fx = 0
    x = 1
    while Fx < u:
        Fx = xi_discrete_rv(x)
        x+=1
    return x-1

print(random_num(3))
print("")

print(xi_discrete_rv(64))
print(xi_discrete_rv(65))
print(xi_discrete_rv(66))

print("")
print(discrete_rv_generator(random_num(3)))

# 2b: Continuous Random Variable
def xi_continuous_rv(u):
    Ft = -12 * np.log(1-u)
    return Ft
