# Jennibelle Khuu (kuf3yd) and Esha Nama (esn4wx)

# import math libraries
import math
import numpy as np
import sys
import matplotlib.pyplot as plot

# Section 1: Random Number Generator ---------------------------------------------------------------------

# starting value (seed)
x_0 = 1000
# multiplier
a = 24693
# increment
c = 3517
# modulus
K = 2**17
u = [0.6779,0.1701]
# linear congruential random number generator
def xi_random_num(i):
   if i == 0:
       return ((a)*(x_0)+c) % K
   else:
       return ((a)*xi_random_num(i-1)+c) % K

def random_num(n):
   n = n-1
   num = xi_random_num(n)
   return num / K

sys.setrecursionlimit(100)

print("random_num 1",random_num(1))
print("random_num 2",random_num(2))
print("random_num 3",random_num(3))
print("random_num 4",random_num(4))

def random_num_gen(i):
   count = i
   x = x_0
   while count >= 0:
       if count == 0:
           return x / K
       else:
           x = (a * x + c) % K
       count -= 1

print("random_num_ gen 1",random_num_gen(1))
print("random_num_ gen 2",random_num_gen(2))
print("random_num_ gen 3",random_num_gen(3))
print("random_num_ gen 4",random_num_gen(4))


# Section 2: Random Variable Generator
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

# Section 3: Mathematical Model
def simulation(run_num):
   w = 0
   num_calls = 1

   random_number = random_num_gen(run_num)

   while True:
       if random_number < 0.2:
           w += 10
           run_num += 1
           random_number = random_num_gen(run_num)
           if num_calls >= 4:
               return w
       elif random_number > 0.2 and random_number < 0.5:
           w += 32
           run_num += 1
           random_number = random_num_gen(run_num)
           if num_calls >= 4:
               return w
       else:
           x = -12 * math.log(1 - random_number)
           if x > 25:
               w += 32
               run_num += 1
               random_number = random_num_gen(run_num)
               if num_calls >= 4:
                   return w
           else:
               w += 6 + x
               return w
       num_calls += 1

def simulate_n_times(n):
   run_num = []
   rand_nums_generated = []
   for k in range(0, n):
       run_num.append(simulation(k))
   return run_num


for x in range(10):
   print(simulation(x))

def simulate_n_times(n):
   w_times = []
   rand_nums_generated = []

   for k in range(0, n):
       w_times.append(simulation(k))

   return w_times


def less_than(w_times, val):
   count = 0
   for i in w_times:
       if i <= val:
           count += 1
   return count


def greater_than(w_times, val):
   count = 0
   for i in w_times:
       if i > val:
           count += 1
   return count


def collect_data(n):
       w_times = simulate_n_times(n)
       mean = np.mean(w_times)
       median = np.median(w_times)
       first_quartile = np.percentile(w_times, 25)
       third_quartile = np.percentile(w_times, 75)
       w15 = less_than(w_times, 15)
       w20 = less_than(w_times, 20)
       w30 = less_than(w_times, 30)
       w40 = greater_than(w_times, 40)
       w5 = greater_than(w_times, 60)
       w6 = greater_than(w_times, 110)
       w7 = greater_than(w_times, 125)

       print("Mean: {}".format(mean))
       print("Median: {}".format(median))
       print("First Quartile: {}".format(first_quartile))
       print("Third Quartile: {}".format(third_quartile))
       print("W <= 15: {}".format(w15 / 1000))
       print("W <= 20: {}".format(w20 / 1000))
       print("W <= 30: {}".format(w30 / 1000))
       print("W > 40: {}".format(w40 / 1000))
       print("W > W5 ({}): {}".format(60, w5 / 1000))
       print("W > W6 ({}): {}".format(110, w6 / 1000))
       print("W > W7 ({}): {}".format(127, w7 / 1000))

       w25 = less_than(w_times, 25)
       w35 = less_than(w_times, 35)
       w45 = less_than(w_times, 45)
       w55 = less_than(w_times, 55)
       w65 = less_than(w_times, 65)
       w75 = less_than(w_times, 75)

       w80 = less_than(w_times, 80)
       w85 = less_than(w_times, 85)
       w90 = less_than(w_times, 90)
       w95 = less_than(w_times, 95)
       w100 = less_than(w_times, 100)
       w105 = less_than(w_times, 105)
       w110 = less_than(w_times, 110)
       w115 = less_than(w_times, 115)
       w120 = less_than(w_times, 120)

       w125 = less_than(w_times, 125)
       w130 = less_than(w_times, 130)
       w135 = less_than(w_times, 135)
       w140 = less_than(w_times, 140)


       print("W <= 25: {}".format(w25 / 1000))
       print("W <= 35: {}".format(w35 / 1000))
       print("W <= 45: {}".format(w45 / 1000))
       print("W <= 55: {}".format(w55 / 1000))
       print("W <= 65: {}".format(w65 / 1000))
       print("W <= 75: {}".format(w75 / 1000) + "\n")

       print("{}".format(w80 / 1000))
       print("{}".format(w85 / 1000))
       print("{}".format(w90 / 1000))
       print("{}".format(w95 / 1000))
       print("{}".format(w100 / 1000))
       print("{}".format(w105 / 1000))
       print("{}".format(w110 / 1000))
       print("{}".format(w115 / 1000))
       print("{}".format(w120 / 1000)+"\n")

       print("{}".format(w125 / 1000))
       print("{}".format(w130 / 1000))
       print("{}".format(w135 / 1000))
       print("{}".format(w140 / 1000))

       print(w_times)

collect_data(1000)

