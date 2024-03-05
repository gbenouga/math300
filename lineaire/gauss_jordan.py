#coding:utf-8
# -*- coding:utf -*-
import numpy as np

def gauss_jordan(A, b):
    n = len(A)
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1)

    for i in range(n):
        pivot_row = i
        for j in range(i+1, n):
            if abs(Ab[j, i]) > abs(Ab[pivot_row, i]):
                pivot_row = j
        Ab[[i, pivot_row]] = Ab[[pivot_row, i]]
        pivot = Ab[i, i]
        Ab[i] /= pivot
        for j in range(n):
            if j != i:
                Ab[j] -= Ab[j, i] * Ab[i]

    x = Ab[:, -1]
    print("la solution est le couple", x)
    return x

# Exemple d'utilisation
A = np.array([[2, 1, -1], [4, -1, 3], [1, 3, -2]])
b = np.array([1, 7, 5])

x = gauss_jordan(A, b)
print("Solution:", x)
