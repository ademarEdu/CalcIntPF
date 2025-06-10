import math

# f(x)=If(0≤x≤1.05, -1.5241676498408 x^(2)+3.2122009718348 x+2.8281986782832)

# Define your variable values here
a = -1.5241676498408
b = 3.2122009718348
c = 2.8281986782832
A = 0
B = 1.05

# Define the expression inside the brackets as a function
def integrate(x, a, b, c):
    result = (a**2 * x**5) / 5
    result += (b**2 * x**3) / 3
    result += (c**2 * x)
    result += (2 * a * b * x**4) / 4
    result += (2 * a * c * x**3) / 3
    result += (2 * b * c * x**2) / 2
    return result

# Evaluate the definite integral from A to B
def get_volume1():
    return math.pi * (integrate(B, a, b, c) - integrate(A, a, b, c))

if __name__ == "__main__":
    result = get_volume1()

    # Print the result
    print(f"El resultado de la integral definida desde A={A} hasta B={B} es: {result}")
