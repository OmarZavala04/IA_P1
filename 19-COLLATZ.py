print("=== SIMULADOR DE LA CONJETURA DE COLLATZ ===")

c0 = int(input("Ingresa un número inicial: "))
pasos = 0

print("\nSecuencia generada:")

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    
    print("→", c0)
    pasos = pasos + 1

print("\nTotal de pasos realizados:", pasos)
print("¡La secuencia llegó a 1!")