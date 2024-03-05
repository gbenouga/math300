#coding:utf-8
# -*- coding:utf -*-
def lagrange(x, y, xi):
    n = len(x)
    yi = 0

    for i in range(n):
        L = 1
        for j in range(n):
            if j != i:
                L *= (xi - x[j]) / (x[i] - x[j])
        yi += y[i] * L

    return yi

