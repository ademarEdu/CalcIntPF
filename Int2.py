import math

# f_{2}(x)=If(1.05<x<4.64, 0.008916672607 x+4.511252358523)

# Define your variable values here
d = 0.008916672607
e = 4.511252358523
A = 1.05
B = 4.64

# Define the expression inside the brackets as a function
def integrate(x, d, e):
    result = (d**2 * x**3) / 3
    result += (2*d*e * x**2) / 2
    result += (e**2 * x)
    return result

# Evaluate the definite integral from A to B
def get_volume2():
    return math.pi * (integrate(B, d, e) - integrate(A, d, e))

if __name__ == "__main__":
    result = get_volume2()

    # Print the result
    print(f"El resultado de la integral definida desde A={A} hasta B={B} es: {result}")
