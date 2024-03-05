import numpy as np

def dolittle(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for k in range(n):
        for j in range(k, n):
            U[k][j] = A[k][j] - sum(L[k][p] * U[p][j] for p in range(k))
        for i in range(k+1, n):
            L[i][k] = (A[i][k] - sum(L[i][p] * U[p][k] for p in range(k))) / U[k][k]

    for i in range(n):
        L[i][i] = 1  # La diagonale de L est fixée à 1

    return L, U

# Exemple d'utilisation
A = np.array([[2, -1, 1], [1, 3, 2], [1, 1, 4]])
L, U = dolittle(A)
print("Matrice L :")
print(L)
print("Matrice U :")
print(U)




import numpy as np

def cholesky(A):
    n = len(A)
    L = np.zeros((n, n))

    for j in range(n):
        for i in range(j, n):
            if i == j:
                L[i][j] = np.sqrt(A[i][j] - sum(L[i][k]**2 for k in range(j)))
            else:
                L[i][j] = (A[i][j] - sum(L[i][k] * L[j][k] for k in range(j))) / L[j][j]

    return L

# Exemple d'utilisation
A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
L = cholesky(A)
print("Matrice L :")
print(L)


import numpy as np

def lu_doolittle(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        L[j][j] = 1
        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A[i][j] - s1
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (A[i][j] - s2) / U[j][j]

    return L, U

# Exemple d'utilisation
A = np.array([[2, -1, 1], [1, 3, 2], [1, 1, 4]])
L, U = lu_doolittle(A)
print("Matrice L :")
print(L)
print("Matrice U :")
print(U)



import numpy as np

def lu_crout(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        U[j][j] = 1
        for i in range(j, n):
            s1 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = A[i][j] - s1
        for i in range(j+1, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            U[i][j] = (A[i][j] - s2) / L[j][j]

    return L, U

# Exemple d'utilisation
A = np.array([[2, -1, 1], [1, 3, 2], [1, 1, 4]])
L, U = lu_crout(A)
print("Matrice L :")
print(L)
print("Matrice U :")
print(U)


import numpy as np

def lu_gauss_pivot(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        max_index = np.argmax(abs(A[j:, j])) + j
        A[[j, max_index]] = A[[max_index, j]]  # Échange des lignes pour le pivot partiel
        for i in range(j, n):
            U[j][i] = A[j][i]
            for k in range(j):
                U[j][i] -= L[j][k] * U[k][i]
        for i in range(j+1, n):
            L[i][j] = A[i][j] / U[j][j]
            for k in range(j):
                L[i][j] -= L[i][k] * U[k][j]

    return L, U

# Exemple d'utilisation
A = np.array([[2, -1, 1], [1, 3, 2], [1, 1, 4]])
L, U = lu_gauss_pivot(A)
print("Matrice L :")
print(L)
print("Matrice U :")
print(U)


def divided_differences(x, y):
    """
    Calcul des différences divisées.

    Args:
    x (list): Liste des coordonnées x des points de données.
    y (list): Liste des coordonnées y des points de données.

    Returns:
    list: Liste des différences divisées.
    """
    n = len(x)
    F = [[0] * n for _ in range(n)]

    # Initialisation de la première colonne avec les valeurs y
    for i in range(n):
        F[i][0] = y[i]

    # Calcul des différences divisées
    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i+1][j-1] - F[i][j-1]) / (x[i+j] - x[i])

    return [F[0][i] for i in range(n)]

def newton_interpolation(x, y, x_interp):
    """
    Interpolation de Newton pour les valeurs x_interp.

    Args:
    x (list): Liste des coordonnées x des points de données.
    y (list): Liste des coordonnées y des points de données.
    x_interp (list): Liste des coordonnées x pour lesquelles interpoler les valeurs y.

    Returns:
    list: Liste des valeurs interpolées correspondant aux coordonnées x_interp.
    """
    F = divided_differences(x, y)
    n = len(x)
    interpolated_values = []

    for xi in x_interp:
        yi = F[0]
        for i in range(1, n):
            term = F[i]
            for j in range(i):
                term *= (xi - x[j])
            yi += term
        interpolated_values.append(yi)

    return interpolated_values

# Exemple d'utilisation
x_data = [0, 1, 2, 3, 4]
y_data = [0, 2, 4, 6, 8]
x_interp = [0.5, 1.5, 2.5, 3.5]
interpolated_values = newton_interpolation(x_data, y_data, x_interp)
print(interpolated_values)



def lagrange_term(x_data, y_data, x, i):
    """
    Calcule le terme de Lagrange correspondant au point de données (x_i, y_i).

    Args:
    x_data (list): Liste des coordonnées x des points de données.
    y_data (list): Liste des coordonnées y des points de données.
    x (float): Valeur à interpoler.
    i (int): Indice du point de données (x_i, y_i) à considérer.

    Returns:
    float: Valeur du terme de Lagrange correspondant au point de données (x_i, y_i).
    """
    term = 1
    for j in range(len(x_data)):
        if j != i:
            term *= (x - x_data[j]) / (x_data[i] - x_data[j])
    return term

def lagrange_interpolation(x_data, y_data, x_interp):
    """
    Interpolation de Lagrange pour les valeurs x_interp.

    Args:
    x_data (list): Liste des coordonnées x des points de données.
    y_data (list): Liste des coordonnées y des points de données.
    x_interp (list): Liste des coordonnées x pour lesquelles interpoler les valeurs y.

    Returns:
    list: Liste des valeurs interpolées correspondant aux coordonnées x_interp.
    """
    interpolated_values = []
    for x in x_interp:
        interpolated_value = sum(y_data[i] * lagrange_term(x_data, y_data, x, i) for i in range(len(x_data)))
        interpolated_values.append(interpolated_value)
    return interpolated_values

# Exemple d'utilisation
x_data = [0, 1, 2, 3, 4]
y_data = [0, 2, 4, 6, 8]
x_interp = [0.5, 1.5, 2.5, 3.5]
interpolated_values = lagrange_interpolation(x_data, y_data, x_interp)
print(interpolated_values)


def least_squares_interpolation(x_data, y_data, degree):
    """
    Interpolation par la méthode des moindres carrés.

    Args:
    x_data (list): Liste des coordonnées x des points de données.
    y_data (list): Liste des coordonnées y des points de données.
    degree (int): Degré du polynôme à ajuster.

    Returns:
    list: Coefficients du polynôme ajusté.
    """
    # Construction de la matrice de conception (Vandermonde)
    X = []
    for x in x_data:
        row = [x**d for d in range(degree+1)]
        X.append(row)
    
    # Construction du vecteur de valeurs cibles
    y = [[yi] for yi in y_data]

    # Résolution du système d'équations normales
    XtX = [[sum(X[i][k] * X[j][k] for k in range(degree+1)) for j in range(degree+1)] for i in range(degree+1)]
    Xty = [[sum(X[i][k] * y[k][0] for k in range(len(y_data)))] for i in range(degree+1)]

    # Résolution du système d'équations normales
    def gauss_elimination(A, b):
        n = len(A)
        for i in range(n):
            max_index = i
            for j in range(i+1, n):
                if abs(A[j][i]) > abs(A[max_index][i]):
                    max_index = j
            A[i], A[max_index] = A[max_index], A[i]
            b[i], b[max_index] = b[max_index], b[i]
            for j in range(i+1, n):
                factor = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= factor * A[i][k]
                b[j][0] -= factor * b[i][0]
        x = [0] * n
        for i in range(n-1, -1, -1):
            x[i] = b[i][0] / A[i][i]
            for j in range(i-1, -1, -1):
                b[j][0] -= A[j][i] * x[i]
        return x

    beta = gauss_elimination(XtX, Xty)

    return beta

# Exemple d'utilisation
x_data = [0, 1, 2, 3, 4]
y_data = [0, 2, 4, 6, 8]
degree = 2  # Degré du polynôme à ajuster
coeffs = least_squares_interpolation(x_data, y_data, degree)
print("Coefficients du polynôme ajusté :", coeffs)


def least_squares_interpolation(x_data, y_data, degree):
    """
    Interpolation par la méthode des moindres carrés.

    Args:
    x_data (list): Liste des coordonnées x des points de données.
    y_data (list): Liste des coordonnées y des points de données.
    degree (int): Degré du polynôme à ajuster.

    Returns:
    list: Coefficients du polynôme ajusté.
    """
    # Construction de la matrice de conception (Vandermonde)
    X = []
    for x in x_data:
        row = [x**d for d in range(degree+1)]
        X.append(row)
    
    # Construction du vecteur de valeurs cibles
    y = [[yi] for yi in y_data]

    # Résolution du système d'équations normales
    XtX = [[sum(X[i][k] * X[j][k] for k in range(degree+1)) for j in range(degree+1)] for i in range(degree+1)]
    Xty = [[sum(X[i][k] * y[k][0] for k in range(len(y_data)))] for i in range(degree+1)]

    # Résolution du système d'équations normales
    def gauss_elimination(A, b):
        n = len(A)
        for i in range(n):
            max_index = i
            for j in range(i+1, n):
                if abs(A[j][i]) > abs(A[max_index][i]):
                    max_index = j
            A[i], A[max_index] = A[max_index], A[i]
            b[i], b[max_index] = b[max_index], b[i]
            for j in range(i+1, n):
                factor = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= factor * A[i][k]
                b[j][0] -= factor * b[i][0]
        x = [0] * n
        for i in range(n-1, -1, -1):
            x[i] = b[i][0] / A[i][i]
            for j in range(i-1, -1, -1):
                b[j][0] -= A[j][i] * x[i]
        return x

    beta = gauss_elimination(XtX, Xty)

    return beta

# Exemple d'utilisation
x_data = [0, 1, 2, 3, 4]
y_data = [0, 2, 4, 6, 8]
degree = 2  # Degré du polynôme à ajuster
coeffs = least_squares_interpolation(x_data, y_data, degree)
print("Coefficients du polynôme ajusté :", coeffs)




