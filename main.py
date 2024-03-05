#coding:utf-8
# -*- coding:utf -*-
import sys


### variables liés au chemin
autres = './mathematique/autres/'
sys.path.append(autres)

from dot import *

# Exemple d'utilisation : création d'une fonction pour le polynôme 2x^2 + 3x + 1
mon_polynome = fonction_return(0, 3, 1,2)

# Utilisation de la fonction polynomiale
print(mon_polynome)
x_valeur = 2
resultat = mon_polynome(x_valeur)

