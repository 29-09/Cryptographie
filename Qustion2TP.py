def square_and_multiply(x, b, n):
    # Convertir n en binaire
    binary_n = bin(n)[2:]

    # Initialiser le résultat à x (mod n)
    result = x % n

    # Parcourir la représentation binaire de n
    for i in range(1, len(binary_n)):
        # Si le bit est 0, effectuer une opération de carré
        if binary_n[i] == "0":
            result = (result ** 2) % n
        # Sinon, effectuer une opération de multiplication et carré
        else:
            result = (result ** 2 * x) % n

    return result
print("Le nombre est de la forme : x exposant n (mod b)")
# L'utilisateur insère les valeurs de x, b et n
x = int(input("Entrez la valeur de x : "))
b = int(input("Entrez la valeur de b : "))
n = int(input("Entrez la valeur de n : "))

# Appeler la fonction square_and_multiply
resultat = square_and_multiply(x, b, n)

# Afficher le résultat
print(f"Le résultat de {x} exposant {n} (mod {b}) est : {resultat}")
