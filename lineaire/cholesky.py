#coding:utf-8
# -*- coding:utf -*-
import numpy as np

def cholesky_custom(A):
    n = len(A)
    L = np.zeros_like(A)

    for i in range(n):
        for j in range(i+1):
            if i == j:
                L[i][i] = np.sqrt(A[i][i] - np.sum(L[i][:i]**2))
            else:
                L[i][j] = (A[i][j] - np.sum(L[i][:j]*L[j][:j])) / L[j][j]

    return L

def cholesky_solve_custom(A, b):
    L = cholesky_custom(A)
    y = np.zeros_like(b)
    x = np.zeros_like(b)
    n = len(A)
    # Résolution du système Ly = b
    for i in range(n):
        y[i] = (b[i] - np.sum(L[i][:i]*y[:i])) / L[i][i]
    # Résolution du système 
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.sum(L[i+1:][i]*x[i+1:])) / L[i][i]
    print("la solution du systeme est : ", x)
    return x

