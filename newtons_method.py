def newton(f, Df, x0, epsilon, max_iter):
    xn = x0
    steps = [xn]  # Store intermediate steps
    for n in range(max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after', n, 'iterations.')
            return xn, steps
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn / Dfxn
        steps.append(xn)  # Append the new step to the list
    print('Exceeded maximum iterations. No solution found.')
    return None, steps