def saisir_matrice():
    while True:
        try:
            # Demander à l'utilisateur de saisir le degré de la matrice
            degre = int(input("Veuillez saisir le degré de la matrice : "))
            
            # S'assurer que le degré est un entier positif
            if degre <= 0:
                raise ValueError("Le degré de la matrice doit être un entier positif.")
            
            # Initialiser une matrice vide
            matrice = []

            # Demander à l'utilisateur de saisir les éléments de la matrice
            for i in range(degre):
                ligne = []
                for j in range(degre):
                    valeur = float(input(f"Veuillez saisir l'élément ({i+1}, {j+1}) de la matrice : "))
                    ligne.append(valeur)
                matrice.append(ligne)

            # Retourner la matrice saisie
            return matrice
        except ValueError as e:
            print(f"Erreur : {e}")

# Appeler la fonction pour saisir une matrice
matrice_saisie = saisir_matrice()

# Afficher la matrice saisie
print("Matrice saisie :")
i=0
for ligne in matrice_saisie:
    i=i+1
    print(ligne, i)