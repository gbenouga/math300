#coding:utf-8
# -*- coding:utf -*-
def secante(f, a, b, epsilon, max_iterations):
    x0 = a
    x1 = b
    i = 0

    while abs(f(x1)) > epsilon and i < max_iterations:
        if f(x1) - f(x0) == 0:
            raise ValueError("La méthode de la sécante ne peut pas être appliquée lorsque f(x1) - f(x0) est égal à zéro.")
        
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        i += 1

    if i == max_iterations:
        raise ValueError("La méthode de la sécante n'a pas convergé après le nombre maximum d'itérations.")

    print("la methode de la sécante admet une solution x0: ", x1, "à la {i} ième itération")

secante(f=lambda x: x**2 -1, a=-2, b=2, epsilon=0.0001, max_iterations=1000)
