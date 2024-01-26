#La media armónica de una secuencia de n números reales x1,x2,…,xn se deﬁne como:

# H= n / (1 / x1) + (1 / x2) + (1 / x3) + (...) + (1 / xn)

# Desarrolle un programa que calcule la media armónica de una secuencia de números. El programa primero debe preguntar al usuario cuántos números ingresará. A continuación, pedirá al usuario que ingrese cada uno de los n números reales. Finalmente, el programa mostrará el resultado.

n = int(input("Cuantos numeros: "))
x = []
for i in range(n):
    x.append(1 / int(input(f"n{i+1} = ")))
print(f"H = {n / sum(x)}")