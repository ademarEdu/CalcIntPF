import math

# l2={3.6931830575095+sqrt(0.3593707639315-x^(2))}

# Assign values to the variables
y_K = 3.6931830575095     # This is y(K)
r_c = math.sqrt(0.3593707639315)      # Radius constant
A = -r_c        # Lower limit
B = r_c        # Upper limit

# Define the full expression inside the brackets as a function
def integrate(x, y_K, r_c):
    result = y_K**2 * x
    arcsin_val = math.asin(x / r_c)
    result += y_K * r_c**2 * (arcsin_val + 0.5 * math.sin(2 * arcsin_val))
    result += r_c * x
    result += -(x**3) / 3
    return result

# Evaluate the definite integral from A to B
def get_volume6():
    return math.pi * (integrate(B, y_K, r_c) - integrate(A, y_K, r_c))

if __name__ == "__main__":
    result = get_volume6()

    # Print the result
    print(f"El resultado de la integral definida desde A={A} hasta B={B} es: {result}")
