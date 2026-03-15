import os
os.system('cls')  # limpia pantalla

print("=== Evaluación de la función ===")
print("f(x) = 3x³ - 2x² + 3x - 1\n")

# valores de x
x_valores = [0, 1, -1]

contador = 1

for x in x_valores:
    x = float(x)
    y = 3 * x**3 - 2 * x**2 + 3 * x - 1
    print(contador, ".- x =", x, "-> y =", y)
    contador += 1