import decimal
from compare import comp

"""Initial variables for the Algorithm"""
buffer = 5
decimals = 1000000 + buffer             # Total precision for decimal calculations (significant digits)
decimal.getcontext().prec = decimals

inital_a = decimal.Decimal("1")
inital_b = decimal.Decimal("1") / decimal.Decimal("2").sqrt()
inital_t = decimal.Decimal("1") / decimal.Decimal("4")
inital_p = decimal.Decimal("1")

total_a = 0
last_a = 0
total_b = 0
total_t = 0
total_p = 0

k = 0
pi = 0

def calc_pi():
    """Calculates Pi with the Gauss-Legendre-Algorithm"""
    
    # Calculate values for the first iteration
    total_a = (inital_a + inital_b) / decimal.Decimal("2")
    last_a = total_a
    total_b = (inital_a * inital_b).sqrt()
    total_t = inital_t - (inital_p * ((inital_a - total_a) * (inital_a - total_a)))
    total_p = decimal.Decimal("2") * inital_p
    #-----------------------------------------
    
    for k in range(20):
        # Main iteration loop for the algorithm
        print("iteration", k)
        total_a = (total_a + total_b) / decimal.Decimal("2")
        total_b = decimal.Decimal(last_a * total_b).sqrt()
        total_t = total_t - (total_p * ((last_a - total_a) * (last_a - total_a)))
        last_a = total_a
        total_p = decimal.Decimal("2") * total_p
        
    # Gets Pi with the end values from the loop above
    pi = ((total_a + total_b) * (total_a + total_b)) / (decimal.Decimal("4") * total_t)
    with open("calcpi.txt", "w") as file:
        file.write(str(pi))
        if pi != 0:
            comp(decimals)

if __name__ == "__main__":
    calc_pi()