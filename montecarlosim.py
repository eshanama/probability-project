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

# Section 2: Random Variable Generator --------------------------------------------------------------------------------
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

# 2b: Continuous Random Variable
def xi_continuous_rv(u):
    Ft = -12 * np.log(1-u)
    return Ft

# Section 3: Mathematical Model ---------------------------------------------------------------------------------------

def simulation(run_num):
    w = 0
    num_calls = 1
    random_number = random_num(run_num)

    while True:
        if random_number < 0.2:
            w += 10
            random_number = random_number / 0.2
            if num_calls >= 4:
                return w
        elif random_number > 0.2 and random_number < 0.5:
            w += 32
            random_number = (random_number - 0.2) / 0.3
            if num_calls >= 4:
                return w
        else:
            Ft = xi_continuous_rv(random_number)
            if Ft > 25:
                w += 32
                random_number = (random_number - 0.5) / 0.5
                if num_calls >= 4:
                    return w
                else:
                    w += 6 + Ft
                    return w
        num_calls += 1

print(random_num(1))
print(simulation(1))