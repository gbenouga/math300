#coding:utf-8
# -*- coding:utf -*-
import numpy as np

def gauss_elimination_1(A, b):
    n = len(A)
    for i in range(n):
        if A[i][i] == 0:
            raise ValueError("La matrice A n'est pas inversible.")
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] -= ratio * A[i][k]
            b[j] -= ratio * b[i]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i):
            b[j] -= A[j][i] * x[i]
    return x

def gauss_elimination(A, B):
    n = len(A)
    for i in range(n):
        # Recherche de la ligne pivot
        max_index = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j
        
        # Échange des lignes
        A[[i, max_index]] = A[[max_index, i]]
        B[[i, max_index]] = B[[max_index, i]]
        
        # Élimination des variables
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            A[j] -= ratio * A[i]
            B[j] -= ratio * B[i]
    
    # Résolution du système triangulaire supérieur
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (B[i] - np.dot(A[i][i+1:], x[i+1:])) / A[i][i]
    
    return x
