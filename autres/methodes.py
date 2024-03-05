#coding:utf-8
# -*- coding:utf -*-
import sys
import math
from sympy import diff, symbols
sys.path.append('..')
import docx
import sympy as sp


eq_non_lineaire = '../autres/'
sys.path.append(eq_non_lineaire)

from autres import *

def is_inversible(a):
    det_A = np.linalg.det(A)
    if det_A != 0:
        return True
    else:
        return False