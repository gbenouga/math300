#coding:utf-8
# -*- coding:utf -*-
import numpy as np

def LU_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1
        U[i][0] = A[i][0]

        for j in range(1, i+1):
            U[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(j))
            L[i][j] = (A[i][j] - sum(L[i][k]*U[k][j] for k in range(j))) / U[j][j]

        for j in range(i+1, n):
            U[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(j))
            L[j][i] = (A[j][i] - sum(L[j][k]*U[k][i] for k in range(i))) / U[i][i]

    return L, U

def substitution_avant(L, b):
    n = len(L)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(L[i][j]*y[j] for j in range(i))) / L[i][i]
    return y

def substitution_arriere(U, y):
    n = len(U)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][j]*x[j] for j in range(i+1, n))) / U[i][i]
    return x

def LU_interpolation(x, y, z):
    n = len(x)
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i][j] = x[i]**j
    L, U = LU_decomposition(A)
    b = substitution_avant(L, y)
    a = substitution_arriere(U, b)
    print("La valeur interpolée en z = {} est :".format(z))
    print(sum(a[i]*z**i for i in range(n)))
    return sum(a[i]*z**i for i in range(n))