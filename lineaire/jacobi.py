#coding:utf-8
# -*- coding:utf -*-

def dot_product(v1, v2):
    # Produit scalaire entre deux vecteurs
    return sum(x * y for x, y in zip(v1, v2))

def matrix_vector_product(matrix, vector):
    # Produit matriciel entre une matrice et un vecteur
    return [dot_product(row, vector) for row in matrix]

def jacobi(A, B, tol=1e-10, max_iter=1000):
    n = len(B)
    X = [0.0] * n  # Initialisation du vecteur solution

    for _ in range(max_iter):
        X_old = X.copy()

        for i in range(n):
            sigma = dot_product(A[i][:i], X_old[:i]) + dot_product(A[i][i+1:], X_old[i+1:])
            X[i] = (B[i] - sigma) / A[i][i]

        # Critère de convergence
        norm_inf = max(abs(x - y) for x, y in zip(X, X_old))
        if norm_inf < tol:
            print(f"La méthode de Jacobi a convergé en {_+1} itérations.")  # Affichage du nombre d'itérations
            print(f" la Solution est : {X}")

    raise ValueError("La méthode de Jacobi n'a pas convergé dans le nombre maximal d'itérations.")

