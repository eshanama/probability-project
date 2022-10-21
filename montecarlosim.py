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
def xi_equation(i):
    if i == 0:
        return ((a)*(x_0)+c) % K
    else:
        return ((a)*xi_equation(i-1)+c) % K

def random_num(n):
    num = xi_equation(n)
    return num / K

# checking first three random numbers
print("u_0: " + str(random_num(0)))     # should be 0.4195
print("u_1: " + str(random_num(1)))     # should be 0.0425
print("u_2: " + str(random_num(2)) + "\n")     # should be 0.1274

print("u_51: " + str(random_num(51)))
print("u_52: " + str(random_num(52)))
print("u_53: " + str(random_num(53)))

# Section 2: Random Variable Generator -------------------------------------------------------------------