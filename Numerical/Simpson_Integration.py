from sympy import sympify, symbols
x = symbols("x")

def function(input):
    return func.subs(x, input)

#iteration number must be even
def simpsonIntegration(upper, lower, iteration):
    evens_Sum = 0
    odds_Sum = 0
    deltaX  = (upper - lower) / iteration
    for even in range(1, iteration, 2):
        evens_Sum += function(lower + (even * deltaX))
    for odd in range(2, iteration - 1, 2):
        odds_Sum  += function(lower + (odd * deltaX))
    return (deltaX / 3) * (function(lower) + (4 * evens_Sum) + (2 * odds_Sum) + function(upper))

expression = input("Function: ")
upper = float(input("Upper Limit: "))
lower = float(input("Lower Limit: "))
iteration = int(input("Iteration: "))
func = sympify(expression)

print(simpsonIntegration(upper, lower, iteration))