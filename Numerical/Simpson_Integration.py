import math
#iteration number must be even
def function(input):
    #current function = sin(x) to the power of 0.5
    return math.sin(pow(input, 0.50000))
def simpsonIntegration(upper, lower, iteration):
    evens_Sum = 0
    odds_Sum = 0
    deltaX  = (upper - lower) / (iteration * 3.00000)
    for even in range(2, iteration, 2):
        evens_Sum = function(lower + (even * deltaX)) + evens_Sum
    for odd in range(3, iteration - 1, 2):
        odds_Sum  = function(lower + (odd * deltaX)) + odds_Sum
    return deltaX * (function(lower) + (2 * evens_Sum) + (4 * odds_Sum) + function(upper))
upper = int(input("Upper Limit: "))
lower = int(input("Lower Limit: "))
iteration = int(input("Iteration: "))
print(simpsonIntegration(upper, lower, iteration))