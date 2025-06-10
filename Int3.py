import math

# g(x)=If(4.64≤x<5.63, 1.7132333965154 x^(3)-26.3951359880167 x^(2)+134.2769215940292 x-221.36303667326)

# Assign values to the variables
f = 1.7132333965154
g = -26.3951359880167
h = 134.2769215940292
i = -221.36303667326
A = 4.64
B = 5.63

# Define the expression inside the brackets as a function
def integrate(x, f, g, h, i):
    result = (f**2 * x**7) / 7
    result += (2 * f * g * x**6) / 6
    result += ((2 * f * h + g**2) * x**5) / 5
    result += ((2 * f * i + 2 * g * h) * x**4) / 4
    result += ((2 * g * i + h**2) * x**3) / 3
    result += (2 * h * i * x**2) / 2
    result += i**2 * x
    return result

# Evaluate the definite integral from A to B
def get_volume3():
    return math.pi * (integrate(B, f, g, h, i) - integrate(A, f, g, h, i))

if __name__ == "__main__":
    result = get_volume3()

    # Print the result
    print(f"El resultado de la integral definida desde A={A} hasta B={B} es: {result}")
