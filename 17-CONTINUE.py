print("=== FILTRO DE VOCALES ===")

palabra = input("Ingresa una palabra cualquiera: ")
palabra = palabra.upper()

print("\nConsonantes encontradas:")

for letra in palabra:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    print(letra)

print("\nProceso terminado.")