#coding:utf-8
# -*- coding:utf -*-
def point_fixe(g, x0, epsilone, max_iterations):
    """
    Méthode du point fixe pour trouver une solution à l'équation f(x) = x.
    
    Args:
        g (function): La fonction g(x) = x.
        x0 (float): La valeur initiale.
        epsilon (float): La précision souhaitée.
        max_iterations (int): Le nombre maximum d'itérations.
    
    Returns:
        float: La solution approximative du point fixe.
    """
    x = x0
    iteration = 0
    y = g(x0)
    while (abs(y - x)/y) > epsilone and iteration < max_iterations:
        x0 = x
        x = g(x)
        iteration += 1
        print("la valeur trouvé est {} à la {}ième itérations" .format(x, iteration))
        
    if(iteration == max_iterations):
        print("la méthode du point fixe n'a pas convergé")
    else:
        print("la méthode du point fixe a convergé en {} itérations et la solution est {} avec une précision de  {}" .format(iteration, x, epsilone))
    




#Exemple d'utilisation
fonction_exemple = lambda x: -x**3 +x**2 + 2

point_fixe(g=fonction_exemple,x0=1, epsilone=1e-6, max_iterations=100000)