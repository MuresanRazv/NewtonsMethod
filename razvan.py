import numpy as np
import matplotlib.pyplot as plt
from newtons_method import newton

f = lambda x: x**5 - 5*x**4 + 10*x**3 - 10*x**2 + 5*x - 1
Df = lambda x: 5*x**4 - 20*x**3 + 30*x**2 - 20*x + 5

x_min, steps = newton(f, Df, 0, 1e-15, 1000)
print("Minimum at x =", x_min)
print("Minimum value =", f(x_min))

# Plotting the function and the root found by Newton's method
x_values = np.linspace(-3, 3, 400)
y_values = f(x_values)
plt.plot(x_values, y_values, label='f(x) = x^2 - 4x + 4')
plt.scatter(steps, [f(step) for step in steps], color='red', label='Steps of Newton\'s method')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function and Steps of Newton\'s Method')
plt.legend()
plt.grid(True)
plt.show()
