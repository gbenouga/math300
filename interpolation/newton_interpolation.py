#coding:utf-8
# -*- coding:utf -*-
def newton_interpolation(x, y, point):
    n = len(x)
    coefficients = [y[0]]
    for i in range(1, n):
        divided_diff = 0
        for j in range(i):
            product = 1
            for k in range(j):
                product *= (x[i] - x[k])
            divided_diff += (y[i] - coefficients[j]) / product
        coefficients.append(divided_diff)
    
    result = coefficients[0]
    for i in range(1, n):
        product = 1
        for j in range(i):
            product *= (point - x[j])
        result += coefficients[i] * product
    
    return result
