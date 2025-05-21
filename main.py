import math
import decimal

decimal.getcontext().prec = 105


inital_a = 1
inital_b = (1/math.sqrt(2))
inital_t = 1/4
inital_p = 1

total_a = 0
total_b = 0
total_t = 0
total_p = 0

k = 0

def calc_pi():
    
    a = (inital_a + inital_b) / 2
    b = math.sqrt(inital_a * inital_b)
    t = inital_t - (inital_p * ((inital_a - a) * (inital_a - a)))
    p = 2 * inital_p
    
    pi = ((a + b) * (a + b)) / (4 * t)
    print(pi)
    
    for a in range(200):
        break
    
    
calc_pi()