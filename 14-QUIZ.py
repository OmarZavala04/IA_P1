palabra = "python"
progreso = ["_"] * len(palabra)
intentos = 6

print("""
+=====================================+
|        JUEGO TIPO AHORCADO          |
|   Adivina la palabra letra por letra|
+=====================================+
""")

while intentos > 0 and "_" in progreso:
    print("\nPalabra:", " ".join(progreso))
    print("Intentos restantes:", intentos)

    letra = input("Ingresa una letra: ").lower()

    if letra in palabra:
        print("¡Bien! La letra está en la palabra.")
        for i in range(len(palabra)):
            if palabra[i] == letra:
                progreso[i] = letra
    else:
        print("No está esa letra.")
        intentos -= 1

if "_" not in progreso:
    print("\n🎉 ¡Ganaste! La palabra era:", palabra)
else:
    print("\n💀 Perdiste. La palabra era:", palabra)