def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise Exception("La méthode des points fixes n'a pas convergé.")


# Exemple d'utilisation
def g(x):
    return x**2 - 4

solution = fixed_point_iteration(g, x0=1)
print("Solution:", solution)