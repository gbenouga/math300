#coding:utf-8
# -*- coding:utf -*-
import sys


eq_non_lineaire = '../autres/'
sys.path.append(eq_non_lineaire)


def dichotomie(fonction, borne_inf, borne_sup, precision=1e-6, max_iterations=100000):
    """
    Algorithme de dichotomie pour trouver une racine d'une fonction dans un intervalle donné.

    Paramètres:
    - fonction: La fonction dont on cherche la racine.
    - borne_inf: Borne inférieure de l'intervalle de recherche.
    - borne_sup: Borne supérieure de l'intervalle de recherche.
    - precision: Précision souhaitée pour la solution.
    - max_iterations: Nombre maximum d'itérations.

    Returns:
    - La valeur approximative de la racine.
    """
    
    # Vérification si la borne_inf est une racine
    if fonction(borne_inf)  == 0:
        print('la fonction f(x) a pour racine ', borne_inf)
    # Vérification si la borne_sup est une racine
    if fonction(borne_sup) == 0:
        print('la fonction f(x) a pour racine ', borne_sup)

    iteration = 0
    while abs(borne_sup - borne_inf) / 2 > precision and iteration < max_iterations:
        xm = (borne_inf + borne_sup) / 2
        valeur_xm = fonction(xm)

        if valeur_xm == 0:
            print("la valeur trouvé est ", (borne_inf+borne_sup)/2,"avec une ordonné de valeur f(x) = ", fonction((borne_sup+borne_inf)/2))
            print("le nombre maximal d'itération est ", iteration)
            
        elif valeur_xm * fonction(borne_inf) < 0:
            borne_sup = xm
        else:
            borne_inf = xm
        iteration += 1
    # Retourne la valeur approchée de la racine
        print("la valeur trouvé est ", (borne_inf+borne_sup)/2,"avec une ordonné de valeur f(x) = ", fonction((borne_sup+borne_inf)/2))
        print("le nombre maximal d'itération est ", iteration)

#Exemple d'utilisation
fonction_exemple = lambda x: x**2 - 1

#i 2 est une borne, la racine exacte est trouvée en une itération
racine_approximative = dichotomie(fonction_exemple, 0, 2)

print("Racine approximative:", racine_approximative)
