#coding:utf-8
# -*- coding:utf -*-
import numpy as np

def newton(f, f_prime, x0, epsilon=1e-6, max_iterations=100):
    x = x0
    iteration = 0
    while abs(f(x)) > epsilon and iteration < max_iterations:
        x = x - f(x) / f_prime(x)
        iteration += 1

    if abs(f(x)) <= epsilon:
        print("la fonction admet une solution x0: ", x, "à la ",iteration, "ième itération")
    else:
        raise ValueError("La méthode de Newton n'a pas convergé.")

#Exemple d'utilisation          
newton(f=lambda x: x**3 -x**2 +x -2, f_prime=lambda x: 3*x**2 -2*x +1, x0=5, epsilon=0.0001, max_iterations=1000)

