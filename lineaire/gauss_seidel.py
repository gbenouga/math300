#coding:utf-8
# -*- coding:utf -*-
def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Les vecteurs doivent avoir la même longueur.")
    
    result = 0.0
    for x, y in zip(v1, v2):
        result += x * y

    return result

def matrix_vector_product(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("Le nombre de colonnes de la matrice doit être égal à la longueur du vecteur.")
    
    result = [dot_product(row, vector) for row in matrix]

    return result

def gauss_seidel(A, B, tol=1e-10, max_iter=1000):
    n = len(B)
    X = [0.0] * n  # Initialisation du vecteur solution

    for _ in range(max_iter):
        for i in range(n):
            sigma = dot_product(A[i][:i], X[:i]) + dot_product(A[i][i+1:], X[i+1:])
            X[i] = (B[i] - sigma) / A[i][i]

        # Critère de convergence
        norm_inf = max(abs(ax - b) for ax, b in zip(matrix_vector_product(A, X), B))
        if norm_inf < tol:
            print(f"La méthode de Gauss-Seidel a convergé en {_+1} itérations.")
            print(f"La solution est : {X}")
            

    raise ValueError("La méthode de Gauss-Seidel n'a pas convergé dans le nombre maximal d'itérations.")
