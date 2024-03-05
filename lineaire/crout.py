#coding:utf-8
# -*- coding:utf -*-
import numpy as np

def LU_crout(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

        for j in range(i, n):
            sum1 = sum(L[j][k] * U[k][i] for k in range(i))
            U[j][i] = A[j][i] - sum1

        for j in range(i + 1, n):
            sum2 = sum(L[i][k] * U[k][j] for k in range(i))
            L[j][i] = (A[j][i] - sum2) / U[i][i]

    return L, U

def premiere_substitution(L, b):
    n = len(L)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i]
    return y

def deuxieme_substitution(U, y):
    n = len(U)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]
    return x

def lu_crout(A, b):
    L, U = LU_crout(A)
    y = premiere_substitution(L, b)
    x = deuxieme_substitution(U, y)
    print("L = ", L)
    print("U = ", U)
    print(" la solution est : ", x)
    print("la solution est le couple (x,y):" , x, y)
    return x