#coding:utf-8
# -*- coding:utf -*-
import sys

import scipy as sp
import cholesky

eq_non_lineaire = "../non_lineaire/"
autres = "../autres/"
lineaire = "../lineaire/"
sys.path.append(eq_non_lineaire, autres, lineaire)

from newton import *
from dichotomie import *
from point_fixe import *
from secante import *
from gauss import *
from gauss_jordan import *
from jacobi import *
from gauss_seidel import *
from crout import *
from lu import *
###saisir un nombre
def saisie_nombre(texte, errortext):
    while True:
        try:
            nombre = int(input(texte))
            return nombre
        except ValueError:
            print("SVP Veuillez entrer un chiffre")

####saisir une fonction  

def fonction_return(*coefficients):
    
    """
        FONCTION RETURNANT UN POLYNOME
    """
    def fonction(x):
        result = 0
        for i, coef in enumerate(coefficients[::-1]):
            result += coef * (x ** i)
        return result

    return fonction

###calcul de dérivé
def calculate_derivative(f):
    x = sp.symbols('x')
    f = sp.sympify(f)
    f_prime = sp.diff(f, x)
    return f_prime

####saisir une matrice
def saisir_matrice(n, m):
    """Saisir une matrice de taille n x m."""
    matrice = []
    for i in range(n):
        ligne = []
        for j in range(m):
            valeur = float(input(f"Entrez l'élément ({i+1}, {j+1}) : "))
            ligne.append(valeur)
        matrice.append(ligne)
    return matrice

### saisir x, y des interpolations
def saisie_donnees_lagrange():
    n = int(input("Entrez le nombre d'intervalles : "))
    x_points = []
    y_points = []

    for i in range(n):
        x = float(input(f"Entrez la valeur x_{i + 1} : "))
        y = float(input(f"Entrez la valeur y_{i + 1} correspondante à x_{i + 1} : "))
        x_points.append(x)
        y_points.append(y)

    return x_points, y_points

###debut du programe
def startprogramme():
    print("--------------------------VOICI LE PROGRAMME DE RESOLUTIONS DE EQUATIONS DE MATH300----------------")
    print("-------MENU DU PROGRAMME--------")
    print("1-RESOLUTIONS D'ÉQUATIONS NON LINÉAIRES")
    print("2-RESOLUTIONS D'ÉQUATIONS LINEAIRES (MATRICES)")
    print("3-INTERPOLATION ET APPROXIMATION POLYNOMIALE")
    print("4-RESOLUTIONS D'EQUATIONS DIFFÉRENTIELS")
    print("5-QUITTEZ")
    print("tapez 1,2,3,4 ou 5 pour accéder à la partie suivante du programme")
    while True:
        try:
            valeur_decimal = int(input("Veuillez faire votre choix : "))
            break
        except ValueError:
            print("Veuillez saisir un nombre entre 1,2,3,4 ou 5 pour continuez le programme")
    
    match valeur_decimal:
        case 1:
            methEqNonLineaire()
        case 2:
            methEqLineaire()
        case 3:
            methInterpolation()
        case 4:
            methEqDiff()
        case 5:
            quittez()
        case _:
            print("Vous avez entré un chiffre non conseillé, veuillez redémarer le programme")

###resolution d'équations non linéaire
def methEqNonLineaire():
    print("RESOLUTIONS D'ÉQUATIONS NON LINÉAIRE")
    borne_inf = saisie_nombre("veuillez entrer la borne inférieur a:")
    borne_sup = saisie_nombre("Veuillez entrer une borne supérieur b")
    epsilone = saisie_nombre("veuillez entrer l'epsilone eo")
    borne_eq = saisie_nombre("veuillez entrez x0")
    dichotomie(borne_inf=borne_inf, borne_sup=borne_sup, epsilon=epsilone, Nmax=100000, fonction=fonction_return(2,8, 6),)
    point_fixe(x0=borne_eq, epsilon=epsilone, f="x2", max_iterations=100000, g=fonction_return(2,5))
    newton(f=fonction_return(1,2), f_prime=fonction_return(2), x0=borne_eq,epsilon=epsilone)
    secante(f=fonction_return(1), a=borne_sup, b=borne_inf,epsilon=epsilone, max_iterations=10000)
def methEqLineaire():
    print("RESOLUTIONS D'ÉQUATIONS  LINÉAIRE")
    m = saisie_nombre("veuillez entrer le nombre de ligne de la matrice: ")
    p = saisie_nombre("Veuillez entrer le nombre de colonnes de la matrice: ")
    matrice_saisie = saisir_matrice(m,p)
    print("La matrice A que vous avez saisie est :")
    for ligne in matrice_saisie:
        print(ligne)
    print("Veuillez entre la matrice B")
    mp = saisie_nombre("veuillez entrer le nombre de lignes de la matrice: ")
    b= saisir_matrice(mp, 1)
    print("La matrice A que vous avez saisie est :")
    for ligne in matrice_saisie:
        print(ligne)
    gauss_elimination(A=matrice_saisie, B=b)
    gauss_jordan(A=matrice_saisie, b=b)
    jacobi(A=matrice_saisie, B=b, tol=1e-10, max_iter=1000)
    gauss_seidel()
    LU_interpolation()
    lu_crout()
    cholesky()
    
def methInterpolation():
    print("INTERPOLATION ET APPROXIMATION POLYNOMIALE")
    
def methEqDiff():
    return 0
def quittez():
    return 0
            
