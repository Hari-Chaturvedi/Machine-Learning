import numpy as np

# Coefficients of the cubic equation 3x^3 - 5x^2 - 13x + 10
coefficients = [3, -5, -13, 10]

# Finding the roots
roots = np.roots(coefficients)

print(roots)
