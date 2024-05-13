import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**5 - 4.5*x**4 + 9*x**3 - 8*x**2 + 4*x - 1 + 0.1*np.sin(10*x)

def Df(x):
    return 5*x**4 - 18*x**3 + 27*x**2 - 16*x + 4 + 10*np.cos(10*x)

from newtons_method import newton

initial_guesses = [0.1, 0.01, -0.1, -0.01]


x_values = np.linspace(-1.5, 1.5, 400)
y_values = f(x_values)

# Plotting the function and the root found by Newton's method for each initial value
for index, guess in enumerate(initial_guesses):
    x_min, steps = newton(f, Df, guess, 1e-12, 500)


    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label='f(x)', color='red')


    print("Initial guess:", guess)
    print("Minimum at x =", x_min)
    print("Steps taken:", len(steps))
    print("Final step value:", steps[-1])
    print("Minimum value =", f(x_min))
    print("Number of iterations:", len(steps) - 1)
    print("---")


    step_x = np.array(steps)
    step_y = f(step_x)
    ax.plot(step_x, step_y, 'o-', label=f'Steps for guess {guess}')


    if x_min is not None:
        ax.plot(x_min, f(x_min), 'ro')

    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)
    ax.legend()


    plt.title(f'Newton\'s Method Convergence from Guess {guess}')
    plt.show()
