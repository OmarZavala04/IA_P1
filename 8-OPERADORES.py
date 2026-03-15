print("╔══════════════════════════════╗")
print("   CÁLCULO DE EXPRESIÓN")
print("╚══════════════════════════════╝")

print("\nFórmula: y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))\n")

x = float(input("Ingresa el valor de x: "))

if x != 0:
    y = 1.0 / (x + 1.0 / (x + 1.0 / (x + 1.0 / x)))
    print("\nResultado y =", y)
else:
    print("\nError: x no puede ser 0 porque hay divisiones entre x.")

print("\nGracias por usar el programa.")