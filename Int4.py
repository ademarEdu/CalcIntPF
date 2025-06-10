import math

# h(x)=If(5.63≤x<6.1939377609435, -0.0202848485644 x+3.8188261470075)

# Assign values to the variables
j = -0.0202848485644
k = 3.8188261470075
A = 5.63
B = 6.1939377609435

# Define the expression inside the brackets as a function
def integrate(x, j, k):
    result = (j**2 * x**3) / 3
    result += (2 * j * k * x**2) / 2
    result += (k**2 * x)
    return result

# Evaluate the definite integral from A to B
def get_volume4():
    return math.pi * (integrate(B, j, k) - integrate(A, j, k))

if __name__ == "__main__":
    result = get_volume4()

    # Print the result
    print(f"El resultado de la integral definida desde A={A} hasta B={B} es: {result}")
