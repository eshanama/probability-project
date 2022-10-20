# Jennibelle Khuu (kuf3yd) and Esha Nama (esn4wx)

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
def random_num(i):
    if i == 0:
        return ((a)*(x_0)+c) % K
    else:
        return random_num(i-1)

print(random_num(1))
